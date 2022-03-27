import os


class Config:
    VERBOSE = bool(os.environ.get("VERBOSE_FLASK"))
    MONGO_URI = os.environ["MONGO_URI"]
    DB_NAME = os.environ["DB_NAME"]
