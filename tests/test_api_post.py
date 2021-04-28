"""
Test CREATE Operation of the API.

Covers
------
- "/<audioFileType>/<audioFileID>" for Song, Podcast & Audiobook.

Record ID Utilized (For GET/PUT/DELETE tests)
Song: 2,3
Podcast: 2, 3 & 4
Audiobook: 2.

"""


def test_song_2(client):
    """
    POST "/api/song/2"

    Parameters
    ----------
    client: pytest fixture
        Test client pytest fixture

    """
    payload = {
        "name": "Song 2",
        "duration": 200
    }
    assert client.post("/api/song/2", json=payload).status_code == 200


def test_song_3_missing_name(client):
    """
    POST "/api/song/3" + name NULL.

    Parameters
    ----------
    client: pytest fixture
        Test client pytest fixture

    """
    payload = {
        "duration": 200
    }
    assert client.post("/api/song/3", json=payload).status_code == 400


def test_podcast_2_wo_participants(client):
    """
    POST "/api/podcast/2"

    Parameters
    ----------
    client: pytest fixture
        Test client pytest fixture

    """
    payload = {
        "name": "Podcast 2",
        "duration": 2000,
        "host": "Podcast Host 2",
    }
    assert client.post("/api/podcast/2", json=payload).status_code == 200


def test_podcast_3_w_participants(client):
    """
    POST "/api/podcast/3"

    Parameters
    ----------
    client: pytest fixture
        Test client pytest fixture

    """
    payload = {
        "name": "Podcast 2",
        "duration": 3000,
        "host": "Podcast Host 2",
        "participants": ["Podcast Participant 1", "Podcast Participant 1"]
    }
    assert client.post("/api/podcast/3", json=payload).status_code == 200


def test_podcast_4_missing_name(client):
    """
    POST "/api/podcast/4" + name NULL.

    Parameters
    ----------
    client: pytest fixture
        Test client pytest fixture

    """
    payload = {
        "duration": 4000,
        "host": "Podcast Host 4",
        "participants": ["Podcast Participant 1", "Podcast Participant 1"]
    }

    assert client.post("/api/podcast/4", json=payload).status_code == 400


def test_audiobook_2(client):
    """
    POST "/api/audio/2"

    Parameters
    ----------
    client: pytest fixture
        Test client pytest fixture

    """

    payload = {
        "name": "Audiobook 2",
        "duration": 2000,
        "author": "Audiobook Author 2",
        "narrator": "Audiobook Narrator 2",

    }

    assert client.post("/api/audiobook/2", json=payload).status_code == 200


def test_audiobook_3_missing_name(client):
    """
    POST "/api/audiobook/4" + name NULL.

    Parameters
    ----------
    client: pytest fixture
        Test client pytest fixture

    """
    payload = {
        "duration": 3000,
        "author": "Audiobook Author 3",
        "narrator": "Audiobook Narrator 3",

    }

    assert client.post("/api/audiobook/3", json=payload).status_code == 400
