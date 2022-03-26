import pymongo
from umongo.frameworks import PyMongoInstance

db_instance = PyMongoInstance()


def get_pymongo_database(app):
    client = pymongo.MongoClient(host=app.config["MONGO_URI"])
    db = client.songs
    return db
