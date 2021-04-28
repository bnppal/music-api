"""
Test DELETE Operation of the API.

Covers
------
- "/<audioFileType>/<audioFileID>" for Song, Podcast & Audiobook.

"""
import json


def test_song_6(client):
    """
    Test DELETE "api/song/6"

    Parameters
    ----------
    client: pytest fixture
        Test client pytest fixture
    """
    # Add Song 6.
    payload = {
        "name": "Song 6",
        "duration": 6000,
    }

    # Add to db.
    client.post("/api/song/6", json=payload)

    # Delete Song 6.
    client.delete("/api/song/6")

    # Check if Deleted.
    resp = client.get("/api/song/6")
    data = json.loads(resp.data)

    assert data == {}


def test_podcast_6(client):
    """
    Test DELETE "api/podcast/6"

    Parameters
    ----------
    client: pytest fixture
        Test client pytest fixture
    """

    # Add Song 6.
    payload = {
        "name": "Podcast 6",
        "duration": 6000,
        "host": "Podcast Host 6",
    }

    # Add to db.
    client.post("/api/podcast/6", json=payload)

    # Delete Podcast 6.
    client.delete("/api/podcast/6")

    # Check if Deleted.
    resp = client.get("/api/podcast/6")
    data = json.loads(resp.data)

    assert data == {}


def test_audiobook_6(client):
    """
    Test DELETE "api/audiobook/6"

    Parameters
    ----------
    client: pytest fixture
        Test client pytest fixture
    """

    # Add Song 6.
    payload = {
        "name": "Audiobook 6",
        "duration": 6000,
        "author": "Audiobook Author 6",
        "narrator": "Audiobook Narrator 6",
    }

    # Add to db.
    client.post("/api/audiobook/6", json=payload)

    # Delete Podcast 6.
    client.delete("/api/audiobook/6")

    # Check if Deleted.
    resp = client.get("/api/audiobook/6")
    data = json.loads(resp.data)

    assert data == {}
