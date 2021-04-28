"""
Test Factory.

Covers
------
- test_config() - Checks if Application initializes when Testing Config is passed.

"""
from phonic import create_app


def test_config():
    """
    Checks if Application initializes when Testing Config is passed.

    """
    # Check if Testing in set by default.
    assert not create_app().testing

    # Check if Passing testing config results in activating testing env.
    assert create_app({"TESTING": True}).testing
