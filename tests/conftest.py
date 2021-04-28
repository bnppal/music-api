"""
Configure Fixtures for Testing.

"""
# Standard Imports.
import os

# Library Imports.
import pytest

# Local Imports.
from phonic import create_app

TEMP_DATABASE_NAME = 'phonic_test_db.sqlite'


@pytest.fixture
def app():
    """
    Flask App for Testing.

    """
    # Grab Database path.
    root_dir = os.path.abspath(os.path.dirname(__file__))
    temp_db_uri = "sqlite:///" + os.path.join(root_dir, TEMP_DATABASE_NAME)

    # Configuring app for testing.
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": temp_db_uri,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    })

    yield app


@pytest.fixture
def client(app):
    """
    Testing Client for testing without running the server.

    """
    return app.test_client()
