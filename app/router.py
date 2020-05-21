from fastapi import APIRouter, Depends, HTTPException, Path
from models import SecretInCreating, SecretInRetrieving
from secret import create_secret, get_secret
from motor.motor_asyncio import AsyncIOMotorClient
from db import get_database

api_router = APIRouter()


@api_router.post("/generate")
async def create(
		secret: SecretInCreating,
		db: AsyncIOMotorClient = Depends(get_database),
):
	"""create new secret"""
	secret_id = await create_secret(secret, db)
	return secret_id


@api_router.post("/secret/{secret_id}")
async def retrieve(
		secret: SecretInRetrieving,
		secret_id: str = Path(..., regex="^[0-9a-fA-F]{24}$"),
		db: AsyncIOMotorClient = Depends(get_database)
):
	"""get secret by secret_id"""
	secret_value = await get_secret(secret_id, secret, db)
	if secret_value is None:
		raise HTTPException(status_code=404, detail="Unknown secret")
	return secret_value
