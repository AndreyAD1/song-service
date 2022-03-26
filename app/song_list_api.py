import logging

from flask import jsonify, request
from umongo import ValidationError

from app import app
from app.models import Song

logger = logging.getLogger(__file__)


@app.route("/api/v1/song", methods=["GET"])
def get_songs():
    songs = [song.dump() for song in Song.find()]
    return jsonify(data=songs)


@app.route("/api/v1/song", methods=["POST"])
def add_song():
    request_data = request.get_json()
    try:
        song = Song(**request_data)
    except ValidationError as ex:
        logger.debug(f"The invalid new song request: {request_data}")
        return jsonify(errors=ex.messages), 400

    song.commit()
    return {}
