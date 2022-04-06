from flask import Blueprint, jsonify, request
from marshmallow import fields, Schema, validate, ValidationError

from app.database import db
from app.services.song_service import SongService

api = Blueprint("difficulty_api", __name__, url_prefix="/api/v1")


class GetDifficultySchema(Schema):
    level = fields.Int(
        as_string=True,
        validate=validate.Range(min=1, max=15),
        allow_none=True
    )


@api.route("/difficulty", methods=["GET"])
def get_average_difficulty():
    level = request.args.get("level")
    try:
        query_args = GetDifficultySchema().load({"level": level})
    except ValidationError as ex:
        return jsonify(errors=ex.messages), 400

    service = SongService(db)
    average_difficulty = service.get_average_difficulty(query_args["level"])
    return jsonify(data={"average_difficulty": average_difficulty})
