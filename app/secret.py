from motor.motor_asyncio import AsyncIOMotorClient
from settings import db_name, secret_collection_name
from security import generate_salt, get_password_hash, verify_password
from models import SecretInCreating
from aes_encryption import AESCipher
from bson.objectid import ObjectId
from typing import Optional


def crypt_secret(secret: SecretInCreating) -> dict:
	salt = generate_salt()
	aes = AESCipher(secret.passphrase)
	secret_db = {
		'salt': salt,
		# без хеширования пароля 7мс, с хешированием через bcrypt 315мс
		'hashed_passphrase': get_password_hash(secret.passphrase + salt),
		'crypted_secret': aes.encrypt(secret.secret)
	}
	return secret_db


def decrypt_secret(secret_crypted, passphrase: str) -> Optional[dict]:

	if verify_password(passphrase + secret_crypted['salt'], secret_crypted['hashed_passphrase']):
		aes = AESCipher(passphrase)
		secret_value = aes.decrypt(secret_crypted['crypted_secret'])
		return {"secret": secret_value}
	else:
		return None


async def save_secret_to_db(secret_db: dict, conn: AsyncIOMotorClient) -> dict:
	answer = await conn[db_name][secret_collection_name].insert_one(secret_db)
	return {'secret_key': str(answer.inserted_id)}


async def get_secret_by_objectid(secret_id: str, conn: AsyncIOMotorClient) -> Optional[dict]:
	return await conn[db_name][secret_collection_name].find_one(filter={'_id': ObjectId(secret_id)})


async def delete_secret_by_objectid(secret_id: str, conn: AsyncIOMotorClient) -> None:
	return await conn[db_name][secret_collection_name].delete_one(filter={'_id': ObjectId(secret_id)})
