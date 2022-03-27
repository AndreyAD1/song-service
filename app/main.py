import logging

from flask import Flask

from app.database import db
from app.config import Config


def get_application():
    application = Flask(__name__)
    application.config.from_object(Config)
    if application.config['VERBOSE']:
        application.logger.setLevel(logging.DEBUG)

    db.instance.set_db(db.get_pymongo_database(application))

    with application.app_context():
        from app.song_list_api import api
        application.register_blueprint(api)
        return application
