from fastapi import APIRouter, Depends, HTTPException, Path
from models import SecretInCreating, SecretInRetrieving, SecretOutCreating, \
	SecretOutRetrieving
from secret import crypt_secret, decrypt_secret, save_secret_to_db,\
	get_secret_by_objectid, delete_secret_by_objectid
from motor.motor_asyncio import AsyncIOMotorClient
from db import get_database

api_router = APIRouter()


@api_router.post("/generate", response_model=SecretOutCreating, status_code=201)
async def create(
		secret: SecretInCreating,
		db: AsyncIOMotorClient = Depends(get_database),
):
	"""create new secret"""
	secret_crypted = crypt_secret(secret)
	secret_id = await save_secret_to_db(secret_crypted, db)
	return secret_id


@api_router.post("/secret/{secret_id}",
				 responses={404: {"description": "Secret not found"}},
				 response_model=SecretOutRetrieving)
async def retrieve(
		secret: SecretInRetrieving,
		secret_id: str = Path(..., regex="^[0-9a-fA-F]{24}$"),
		db: AsyncIOMotorClient = Depends(get_database)
):
	"""get secret by secret_id"""
	secret_crypted = await get_secret_by_objectid(secret_id, db)
	if secret_crypted is None:
		raise HTTPException(status_code=404, detail="Unknown secret")
	secret_value = decrypt_secret(secret_crypted, secret.passphrase)
	if secret_value is None:
		raise HTTPException(status_code=404, detail="Unknown secret")
	await delete_secret_by_objectid(secret_id, db)
	return secret_value
