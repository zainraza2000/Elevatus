from pymongo import MongoClient

from settings import settings


USERNAME = settings.mongo_username
PASSWORD = settings.mongo_password
HOST = settings.mongo_host
PORT = settings.mongo_port

# can add user & password to db here as well
def get_mongodb():
    connection_string = f"mongodb://{HOST}:{PORT}/"
    client = MongoClient(connection_string)
    db = client.storage
    return db
