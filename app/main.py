import logging

from flask import Flask

from app.database import db
from app.config import Config


def get_application():
    application = Flask(__name__)
    application.config.from_object(Config)
    if application.config['VERBOSE']:
        application.logger.setLevel(logging.DEBUG)

    db.set_database(application)

    with application.app_context():
        from app.api.song_list_api import api as song_api
        from app.api.difficulty_api import api as difficulty_api
        application.register_blueprint(song_api)
        application.register_blueprint(difficulty_api)
        return application
