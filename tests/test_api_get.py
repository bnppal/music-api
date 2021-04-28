"""
Test RETRIEVE Operation of the API.

Covers
------
- "/<audioFileType>/<audioFileID>" for Song, Podcast & Audiobook.
- "/<audioFileType>" for Song, Podcast & Audiobook.

"""


def test_specific_song_before_post(client):
    """
    Test "api/song/1"

    Parameters
    ----------
    client: pytest fixture
        Test client pytest fixture

    """
    assert client.get("/api/song/1").status_code == 200


def test_specific_podcast_before_post(client):
    """
    Test "api/podcast/1"

    Parameters
    ----------
    client: pytest fixture
        Test client pytest fixture

    """
    assert client.get("/api/podcast/1").status_code == 200


def test_specific_audiobook_before_post(client):
    """
    Test "api/audiobook/1"

    Parameters
    ----------
    client: pytest fixture
        Test client pytest fixture

    """
    assert client.get("/api/audiobook/1").status_code == 200


def test_all_songs_before_post(client):
    """
    Test "api/song"

    Parameters
    ----------
    client: pytest fixture
        Test client pytest fixture

    """
    assert client.get("/api/song").status_code == 200


def test_all_podcasts_before_post(client):
    """
    Test "api/podcast"

    Parameters
    ----------
    client: pytest fixture
        Test client pytest fixture

    """
    assert client.get("/api/podcast").status_code == 200


def test_all_audiobooks_before_post(client):
    """
    Test "api/audiobook"

    Parameters
    ----------
    client: pytest fixture
        Test client pytest fixture

    """
    assert client.get("/api/audiobook").status_code == 200
