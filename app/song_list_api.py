import logging

from flask import jsonify

from app import app
from app.models import Song

logger = logging.getLogger(__file__)


@app.route("/api/v1/songs", methods=["GET"])
def get_songs():
    songs = [song.dump() for song in Song.find()]
    return jsonify(data=songs)
