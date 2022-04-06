from flask import current_app

from app.constants import DEFAULT_LIMIT
from app.models import Song


class SongService:
    def __init__(self, database):
        self.db = database

    @staticmethod
    def get_song_list(limit=DEFAULT_LIMIT, offset=0):
        return [song.dump() for song in Song.find().skip(offset).limit(limit)]

    def get_average_difficulty(self):
        pipeline = [
            {"$group": {"_id": None, "average": {"$avg": "$difficulty"}}}
        ]
        song_collection = self.db.db_connection[Song.opts.collection_name]
        query_result = list(song_collection.aggregate(pipeline))
        current_app.logger.debug(f"Average difficulty: {query_result}")
        return query_result[0]["average"]
