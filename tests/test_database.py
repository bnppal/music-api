"""
Test Database Instance & Files.

"""
# Standard Imports.
import os


def test_sqlite_file(app):
    """
    Check if test_db is created.

    Parameters
    ---------
    app: fixture.
        Flask App Fixture.

    """
    # Grab abs path of tests/
    root_dir = os.path.abspath(os.path.dirname(__file__))
    temp_db_uri = os.path.join(root_dir, "phonic_test_db.sqlite")

    assert os.path.exists(temp_db_uri)
