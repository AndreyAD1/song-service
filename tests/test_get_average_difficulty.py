import pytest

from tests.utils import add_song


@pytest.mark.parametrize(
    ("difficulties", "expected_avg_difficulty"),
    [
        ([], None),
        ([5], 5),
        ([5, 10], 7.5),
    ],
    ids=[
        "no songs",
        "one song",
        "two songs"
    ]
)
def test_get_average_difficulty(client, difficulties, expected_avg_difficulty):
    for difficulty in difficulties:
        add_song(difficulty=difficulty)

    response = client.get("/api/v1/difficulty")
    response_body = response.get_json()["data"]
    assert response_body["average_difficulty"] == expected_avg_difficulty


@pytest.mark.parametrize(
    ("song_features", "request_level", "expected_avg_difficulty"),
    [
        ([], 5, None),
        ([(10, 5)], 5, 10),
        ([(10, 5)], 1, None),
        ([(10, 5), (15, 5), (3, 1)], 5, 12.5)
    ],
    ids=[
        "no songs",
        "one song",
        "one songs, unsuitable level",
        "three songs"
    ]
)
def test_get_average_difficulty_per_level(
        client,
        song_features,
        request_level,
        expected_avg_difficulty
):
    for difficulty, level in song_features:
        add_song(difficulty=difficulty, level=level)

    query_params = {"level": request_level}
    response = client.get("/api/v1/difficulty", query_string=query_params)
    response_body = response.get_json()["data"]
    assert response_body["average_difficulty"] == expected_avg_difficulty
