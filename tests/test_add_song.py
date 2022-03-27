from deepdiff import DeepDiff
import pytest


@pytest.mark.parametrize(
    ("request_body", "expected_response"),
    [
        (
            {"artist": "The Yousicians", "title": "Lycanthropic Metamorphosis", "difficulty": 14.6, "level": 13, "released": "2016-10-26"},
            {"artist": "The Yousicians", "title": "Lycanthropic Metamorphosis", "difficulty": 14.6, "level": 13, "released": "2016-10-26"}
        ),
        (
            {"title": "Lycanthropic Metamorphosis"},
            {"title": "Lycanthropic Metamorphosis"}
        )
    ],
    ids=("all fields", "only title")
)
def test_add_song(request_body, expected_response, client):
    response = client.post("/api/v1/song", json=request_body)
    assert response.status_code == 200
    received_response = response.get_json()
    assert received_response["id"]
    diff = DeepDiff(received_response, expected_response, exclude_paths="root['id']")
    assert not diff.to_dict()
