import pytest
"""from motor.motor_asyncio import AsyncIOMotorClient
from settings import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT"""


@pytest.fixture()
def init_db():
	pass
	'''db = AsyncIOMotorClient(str(MONGODB_URL),
								   maxPoolSize=MAX_CONNECTIONS_COUNT,
								   minPoolSize=MIN_CONNECTIONS_COUNT)
	yield
	db.close()'''
