import pymongo
from umongo.frameworks import PyMongoInstance


class Database:
    def __init__(self):
        self.instance = PyMongoInstance()
        self.client = None
        self.db_name = None
        self.db = None

    def get_pymongo_database(self, application):
        self.client = pymongo.MongoClient(host=application.config["MONGO_URI"])
        self.db_name = application.config["DB_NAME"]
        self.db = self.client[self.db_name]
        return self.db


db = Database()
