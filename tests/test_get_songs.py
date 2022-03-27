from deepdiff import DeepDiff
import pytest

from tests.utils import add_song
from app.models import Song


@pytest.mark.parametrize(
    "song_number",
    [0, 1, 2],
)
def test_get_songs(client, song_number):
    expected_songs = [dict(add_song().dump()) for _ in range(song_number)]
    response = client.get("/api/v1/song")
    received_result = response.get_json()
    diff = DeepDiff(received_result, {"data": expected_songs})
    assert not diff.to_dict()
