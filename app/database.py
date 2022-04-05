import pymongo
from umongo.frameworks import PyMongoInstance


class Database:
    def __init__(self):
        self.instance = PyMongoInstance()
        self.client = None
        self.db_name = None
        self.db_connection = None

    def set_database(self, application):
        self.client = pymongo.MongoClient(host=application.config["MONGO_URI"])
        self.db_name = application.config["DB_NAME"]
        self.db_connection = self.client[self.db_name]
        self.instance.set_db(self.db_connection)


db = Database()
