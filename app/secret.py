from motor.motor_asyncio import AsyncIOMotorClient
from settings import db_name, secret_collection_name
from security import generate_salt, get_password_hash, verify_password
from models import SecretInCreating, SecretInRetrieving
from aes_encryption import AESCipher
from bson.objectid import ObjectId
from typing import Optional


async def create_secret(secret: SecretInCreating, conn: AsyncIOMotorClient) -> str:
	salt = generate_salt()
	aes = AESCipher(secret.passphrase)
	secret_db = {
		'salt': salt,
		# без хеширования пароля 7мс, с хешированием 315мс
		'hashed_passphrase': get_password_hash(secret.passphrase + salt),
		'crypted_secret': aes.encrypt(secret.secret)
	}
	answer = await conn[db_name][secret_collection_name].insert_one(secret_db)
	return str(answer.inserted_id)


async def get_secret(secret_id: str, secret: SecretInRetrieving, conn: AsyncIOMotorClient) -> Optional[dict]:
	cursor = await conn[db_name][secret_collection_name].find_one(filter={'_id': ObjectId(secret_id)})
	if cursor is None:
		return None
	if verify_password(secret.passphrase + cursor['salt'], cursor['hashed_passphrase']):
		aes = AESCipher(secret.passphrase)
		secret_value = aes.decrypt(cursor['crypted_secret'])
		await conn[db_name][secret_collection_name].delete_one(filter={'_id': ObjectId(secret_id)})
		return {"secret": secret_value}
	else:
		return None

