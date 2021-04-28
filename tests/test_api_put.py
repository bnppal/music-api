"""
Test UPDATE Operation of the API.

Covers
------
- "/<audioFileType>/<audioFileID>" for Song, Podcast & Audiobook.

"""
import json


def test_song_2(client):
    """
    PUT "/api/song/2" + Name Change.

    Parameters
    ----------
    client: pytest fixture
        Test client pytest fixture

    """
    payload = {
        "name": "Song Two",
        "duration": 200
    }
    # Update Song 2 Name.
    client.put("/api/song/2", json=payload)

    # Get Update Name.
    resp = client.get("/api/song/2")
    data = json.loads(resp.data)

    assert data["name"] == "Song Two"


def test_podcast_5(client):
    """
    PUT "/api/podcast/5" + Name Change.

    Parameters
    ----------
    client: pytest fixture
        Test client pytest fixture

    """
    payload = {
        "name": "Podcast 5",
        "duration": 5000,
        "host": "Podcast Host 5",
    }

    # Add to db.
    client.post("/api/podcast/5", json=payload)

    # Update Product 5 Name.
    payload_update = {
        "name": "Podcast Five",
        "duration": 5000,
        "host": "Podcast Host Five",
    }

    client.put("/api/podcast/5", json=payload_update)

    # Get Update Name.
    resp = client.get("/api/podcast/5")
    data = json.loads(resp.data)

    assert data["name"] == "Podcast Five"


def test_audiobook_2(client):
    """
    PUT "/api/audiobook/2" + Name Change.

    Parameters
    ----------
    client: pytest fixture
        Test client pytest fixture

    """
    payload = {
        "name": "Audiobook Two",
        "duration": 2000,
        "author": "Audiobook Author Two",
        "narrator": "Audiobook Narrator Two",
    }

    # Update Audiobook 2 Name.
    client.put("/api/audiobook/2", json=payload)

    # Get Update Name.
    resp = client.get("/api/audiobook/2")
    data = json.loads(resp.data)

    assert data["name"] == "Audiobook Two"
