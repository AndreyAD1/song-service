import logging

from app import app

logger = logging.getLogger(__file__)


@app.route("/ping")
def ping():
    return "<p>Ping</p>"
