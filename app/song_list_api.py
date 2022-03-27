import logging

from flask import Blueprint, jsonify, request, current_app
from umongo import ValidationError

from app.models import Song

logger = logging.getLogger(__file__)

api = Blueprint("song_list_api", __name__, url_prefix="/api/v1")


@api.route("/song", methods=["GET"])
def get_songs():
    songs = [song.dump() for song in Song.find()]
    return jsonify(data=songs)


@api.route("/song", methods=["POST"])
def add_song():
    request_data = request.get_json()
    try:
        song = Song(**request_data)
    except ValidationError as ex:
        current_app.logger.debug(f"The invalid new song request: {request_data}")
        return jsonify(errors=ex.messages), 400

    song.commit()
    return jsonify(song.dump())
