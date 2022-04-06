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
