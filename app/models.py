from umongo import Document, fields

from app import song_db


@song_db.register
class Song(Document):
    artist = fields.StrField()
    title = fields.StrField()
    difficulty = fields.IntField()
    level = fields.IntField()
    released = fields.DateField()
