import pytest

from app.database import db
from app.main import get_application


@pytest.fixture()
def app():
    app = get_application()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    db.client.drop_database(db.db_name)


@pytest.fixture()
def client(app):
    return app.test_client()
