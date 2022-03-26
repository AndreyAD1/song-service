import logging

from flask import jsonify, request, current_app
from umongo import ValidationError

from app.models import Song

logger = logging.getLogger(__file__)


@current_app.route("/api/v1/song", methods=["GET"])
def get_songs():
    songs = [song.dump() for song in Song.find()]
    return jsonify(data=songs)


@current_app.route("/api/v1/song", methods=["POST"])
def add_song():
    request_data = request.get_json()
    try:
        song = Song(**request_data)
    except ValidationError as ex:
        current_app.logger.debug(f"The invalid new song request: {request_data}")
        return jsonify(errors=ex.messages), 400

    song.commit()
    return jsonify(song.dump())
