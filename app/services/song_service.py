from app.constants import DEFAULT_LIMIT
from app.models import Song


class SongService:
    @staticmethod
    def get_song_list(limit=DEFAULT_LIMIT, offset=0):
        return [song.dump() for song in Song.find().skip(offset).limit(limit)]
