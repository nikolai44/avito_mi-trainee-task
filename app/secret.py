from motor.motor_asyncio import AsyncIOMotorClient
from db import get_database
from settings import db_name, secret_collection_name
from security import generate_salt, get_password_hash, verify_password
from models import Secret, SecretInDB
from aes_encryption import AESCipher
from bson.objectid import ObjectId


async def create_secret(secret: Secret, conn: AsyncIOMotorClient) -> str:
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


async def get_secret(secret_key: str, passphrase: str, conn: AsyncIOMotorClient):
	row = await conn[db_name][secret_collection_name].find({'_id': ObjectId(secret_key)})
	print(row)
