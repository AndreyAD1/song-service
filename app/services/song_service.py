import pymongo
from flask import current_app

from app.constants import DEFAULT_LIMIT
from app.models import Song


class SongService:
    def __init__(self, database):
        self.db = database

    @staticmethod
    def get_song_list(limit=DEFAULT_LIMIT, offset=0):
        return [song.dump() for song in Song.find().skip(offset).limit(limit)]

    @property
    def song_collection(self):
        return self.db.db_connection[Song.opts.collection_name]

    def get_average_difficulty(self, level):
        pipeline = []
        if level:
            pipeline.append({"$match": {"level": level}})
        average_query = {
            "$group": {"_id": None, "average": {"$avg": "$difficulty"}}
        }
        pipeline.append(average_query)
        current_app.logger.debug(f"Difficulty pipeline: {pipeline}")
        query_result = list(self.song_collection.aggregate(pipeline))
        current_app.logger.debug(f"Average difficulty: {query_result}")
        average = None
        if query_result:
            average = query_result[0]["average"]
        return average

    def search_song(self, search_query):
        index_features = [("artist", pymongo.TEXT), ("title", pymongo.TEXT)]
        self.song_collection.create_index(index_features)
        pipeline = [
            {
                "$match": {
                    "$text": {"$search": search_query, "$caseSensitive": False}
                }
            },
            {
                "$sort": {
                    "score": {"$meta": "textScore"}
                }
            }
        ]
        songs = list(self.song_collection.aggregate(pipeline))
        return [Song.build_from_mongo(s).dump() for s in songs]
