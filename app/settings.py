import os
from databases import DatabaseURL

SECRET_TOKEN = os.getenv('SECRET_TOKEN', 'not_secure')
ENVIRONMENT = os.getenv('ENVIRONMENT', 'dev')

MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_USER = os.getenv("MONGO_USER", "user")
MONGO_PASS = os.getenv("MONGO_PASSWORD", "admin")
MONGO_DB = os.getenv("MONGO_DB", "fastapi")
MONGODB_URL = DatabaseURL(f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}")
# MONGODB_URL = DatabaseURL(f"mongodb://{MONGO_HOST}:{MONGO_PORT}")
MAX_CONNECTIONS_COUNT = int(os.getenv("MAX_CONNECTIONS_COUNT", 10))
MIN_CONNECTIONS_COUNT = int(os.getenv("MIN_CONNECTIONS_COUNT", 10))

db_name = MONGO_DB
secret_collection_name = 'secrets'
