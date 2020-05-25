import logging
from motor.motor_asyncio import AsyncIOMotorClient
from settings import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT, \
    db_name


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def connect_to_mongo():
    logging.info("try to connect to db")
    print(MONGODB_URL, str(MONGODB_URL))
    db.client = AsyncIOMotorClient(str(MONGODB_URL),
                                   maxPoolSize=MAX_CONNECTIONS_COUNT,
                                   minPoolSize=MIN_CONNECTIONS_COUNT)
    database = db.client[db_name]['secrets'].insert_one({})
    print(database)
    logging.info("successfully connected to db")


async def close_mongo_connection():
    logging.info("start db closing")
    db.client.close()
    logging.info("db closed")


async def get_database() -> AsyncIOMotorClient:
    return db.client
