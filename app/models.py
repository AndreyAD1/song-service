from umongo import Document, fields

from app.database import db


@db.instance.register
class Song(Document):
    artist = fields.StrField()
    title = fields.StrField(required=True)
    difficulty = fields.FloatField()
    level = fields.IntField()
    released = fields.DateField()
