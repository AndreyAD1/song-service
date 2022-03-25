import logging

from config import Config
from flask import Flask

app = Flask(__name__)
app.config.from_object(Config)
if app.config['VERBOSE']:
    app.logger.setLevel(logging.DEBUG)

from app import song_list_api
