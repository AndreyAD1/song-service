from flask import current_app

from app.constants import DEFAULT_LIMIT
from app.models import Song


class SongService:
    def __init__(self, database):
        self.db = database

    @staticmethod
    def get_song_list(limit=DEFAULT_LIMIT, offset=0):
        return [song.dump() for song in Song.find().skip(offset).limit(limit)]

    def get_average_difficulty(self, level):
        pipeline = []
        if level:
            pipeline.append({"$match": {"level": level}})
        average_query = {
            "$group": {"_id": None, "average": {"$avg": "$difficulty"}}
        }
        pipeline.append(average_query)
        song_collection = self.db.db_connection[Song.opts.collection_name]
        current_app.logger.debug(f"Difficulty pipeline: {pipeline}")
        query_result = list(song_collection.aggregate(pipeline))
        current_app.logger.debug(f"Average difficulty: {query_result}")
        average = None
        if query_result:
            average = query_result[0]["average"]
        return average
