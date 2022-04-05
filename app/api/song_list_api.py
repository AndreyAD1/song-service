from flask import Blueprint, jsonify, request, current_app
from marshmallow import fields, Schema, validate
from umongo import ValidationError

from app.constants import DEFAULT_LIMIT
from app.models import Song
from app.services.song_service import SongService

api = Blueprint("song_list_api", __name__, url_prefix="/api/v1")


class GetSongSchema(Schema):
    limit = fields.Int(
        as_string=True,
        validate=validate.Range(min=1, max=DEFAULT_LIMIT)
    )
    offset = fields.Int(as_string=True)


@api.route("/song", methods=["GET"])
def get_songs():
    limit = request.args.get("limit", DEFAULT_LIMIT)
    offset = request.args.get("offset", 0)
    try:
        query_args = GetSongSchema().load({"limit": limit, "offset": offset})
    except ValidationError as ex:
        return jsonify(errors=ex.messages), 400

    songs = SongService().get_song_list(
        query_args["limit"],
        query_args["offset"]
    )
    return jsonify(data=songs)


@api.route("/song", methods=["POST"])
def add_song():
    request_data = request.get_json()
    try:
        song = Song(**request_data)
    except ValidationError as ex:
        error_message = f"The invalid new song request: {request_data}"
        current_app.logger.debug(error_message)
        return jsonify(errors=ex.messages), 400

    song.commit()
    return jsonify(song.dump())


@api.route("/song/difficulty", methods=["GET"])
def get_average_difficulty():
    average_difficulty = SongService.get_average_difficulty()
    return jsonify(data=average_difficulty)
