from flask import current_app

from app.constants import DEFAULT_LIMIT
from app.database import db
from app.models import Song


class SongService:
    @staticmethod
    def get_song_list(limit=DEFAULT_LIMIT, offset=0):
        return [song.dump() for song in Song.find().skip(offset).limit(limit)]

    @staticmethod
    def get_average_difficulty():
        pipeline = [
            {"$group": {"_id": None, "average": {"$avg": "$level"}}}
        ]
        result = list(db.db_connection.song.aggregate(pipeline))
        current_app.logger.debug(f"Average difficulty: {result}")
        return result[0]["average"]
