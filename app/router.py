from fastapi import APIRouter, Depends
from models import Secret
from secret import create_secret, get_secret
from motor.motor_asyncio import AsyncIOMotorClient
from db import get_database

api_router = APIRouter()


@api_router.post("/generate")
async def create(
		secret: Secret,
		db: AsyncIOMotorClient = Depends(get_database),
):
	"""create new secret"""
	secret_id = await create_secret(secret, db)
	return secret_id


@api_router.post("/secret/{secret_id}")
async def retrieve(
		secret_key: str,
		passphrase: str,
		db: AsyncIOMotorClient = Depends(get_database)
):
	"""get secret by secret_id"""
	secret = get_secret(secret_key, passphrase, db)
