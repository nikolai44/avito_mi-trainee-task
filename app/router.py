from fastapi import APIRouter
from models import Secret

api_router = APIRouter()


@api_router.post("/generate")
async def create(secret: Secret):
	"""create secret
	get secret, passphrase and optionally ttl
	return secret_key"""
	return secret


@api_router.post("/secret/{secret_key}")
async def retrieve(secret_key: str):
	pass
