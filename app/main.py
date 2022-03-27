import logging

from flask import Flask

from app.database import db_instance, get_pymongo_database
from app.config import Config


def get_application():
    application = Flask(__name__)
    application.config.from_object(Config)
    if application.config['VERBOSE']:
        application.logger.setLevel(logging.DEBUG)

    db = get_pymongo_database(application)
    db_instance.set_db(db)

    with application.app_context():
        from app import song_list_api
        return application
