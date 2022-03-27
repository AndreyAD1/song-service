from random import uniform, randrange

from faker import Faker

from app.models import Song


def get_faker():
    return Faker()


def add_song(**kwargs):
    faker = get_faker()
    song_features = {
        "artist": faker.name(),
        "title": faker.word(),
        "difficulty": round(uniform(1, 15), 2),
        "level": randrange(1, 15),
        "released": faker.date()
    }
    song = Song(**{**song_features, **kwargs})
    song.commit()
    return song
