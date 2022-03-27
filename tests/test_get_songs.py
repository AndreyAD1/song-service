from deepdiff import DeepDiff
import pytest

from app.constants import DEFAULT_LIMIT
from tests.utils import add_song


@pytest.mark.parametrize(
    "song_number",
    [
        0,
        1,
        2,
        3
    ],
    ids=[
        "0 songs",
        "1 song",
        "2 songs",
        "3 songs"
    ]
)
@pytest.mark.parametrize(
    "limit",
    [
        None,
        1,
        2,
        DEFAULT_LIMIT
    ],
    ids=[
        "no limit",
        "limit=1",
        "limit=2",
        "default limit"
    ]
)
@pytest.mark.parametrize(
    "offset",
    [
        None,
        1,
        2
    ],
    ids=(
        "no offset",
        "offset=1",
        "offset=2"
    )
)
def test_get_songs(client, song_number, limit, offset):
    created_songs = [dict(add_song().dump()) for _ in range(song_number)]
    max_expected_index = (offset or 0) + (limit or len(created_songs))
    expected_songs = created_songs[offset:max_expected_index]
    query_params = {"limit": limit, "offset": offset}
    response = client.get("/api/v1/song", query_string=query_params)
    received_result = response.get_json()
    diff = DeepDiff(received_result, {"data": expected_songs})
    assert not diff.to_dict()
