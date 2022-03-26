import logging

from flask import Flask
import pymongo
from umongo.frameworks import PyMongoInstance

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
if app.config['VERBOSE']:
    app.logger.setLevel(logging.DEBUG)

client = pymongo.MongoClient(host=app.config["MONGO_URI"])
db = client.songs
song_db = PyMongoInstance(db)

from app import song_list_api
