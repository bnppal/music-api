"""
Module to Define Database Data Models & Schemas.

Tables & Schemas
----------------
- Song
- Podcast
- Audiobook

"""
# Standard Imports.
import datetime

# Local Imports.
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


def register_extensions(app):
    """
    Register Flask-SQLAlchemy & Flask-Marshmallow.

    Parameters
    ----------
    app: Flask App Instance.

    """
    # Init database.
    db.init_app(app)

    # Create Data models.
    with app.app_context():
        db.create_all()
        db.session.commit()
        ma.init_app(app)


class Base(db.Model):
    """
    Base Class for Phonic Data Models.
    """
    __abstract__ = True

    id = db.Column(db.Integer,
                   unique=True,
                   primary_key=True,
                   nullable=False)

    name = db.Column(db.String(100),
                     nullable=False)

    duration = db.Column(db.Integer,
                         nullable=False)

    uploaded_time = db.Column(db.DateTime,
                              default=datetime.datetime.utcnow(),
                              nullable=False)

    def __init__(self, id, duration, name):
        """
        Base Data Model.

        Parameters
        ----------
        id: int.
            Identification Number of the audioFile
        duration: int
            Duration of the audioFile
        name: str, max = 100 char, default = None
            Name of the audioFile

        """
        self.id = id
        self.name = name
        self.duration = duration


class Song(Base):
    """
    Song Data Model.

    """

    # todo: validate as a required field.

    def __init__(self, id, name, duration):
        """
        Init Song Data Model.

        Parameters
        ----------
        id: int.
            Identification Number of the Song
        name: str, max = 100 char
            Name of the Song
        duration: int
            Duration of the Song

        """
        super(Song, self).__init__(id=id, name=name, duration=duration)


class Podcast(Base):
    """
    Podcast Data Model.

    """
    # todo: Add Column Validation Layer to Podcast.

    host = db.Column(db.String(100),
                     nullable=False)

    participants = db.Column(db.PickleType,
                             nullable=True)

    def __init__(self, id, name, duration, host, participants=None):
        """
        Init Podcast Data Model.

        Parameters
        ----------
        id: int.
            Identification Number of the Podcast file
        name: str, max = 100 char
            Name of the Podcast
        duration: int
            Duration of the Podcast
        host: str, max = 100 char
            Name of the Podcast Host
        participants: pkl (list of string), max = 10 participants, default=None
            Name of Participants.

        """
        super(Podcast, self).__init__(id=id, name=name, duration=duration)
        self.host = host
        self.participants = participants


class AudioBook(Base):
    """
    AudioBook Data Model.

    """
    # todo: Add Column Validation Layer to Audiobook.

    author = db.Column(db.String(100),
                       nullable=False)

    narrator = db.Column(db.String(100),
                         nullable=False)

    def __init__(self, id, name, author, narrator, duration):
        """
        Init Podcast Data Model.

        Parameters
        ----------
        id: int
            Identification Number of the Audiobook file
        name: str, max = 100 char
            Title of the Audiobook
        author: str, max = 100 char
            Author of the Audiobook
        narrator: str, max = 100 char
            Narrator of the Audiobook
        duration: int,
            Duration of the Audiobook


        """
        super(AudioBook, self).__init__(id=id, name=name, duration=duration)
        self.author = author
        self.narrator = narrator


class SongSchema(ma.Schema):
    """
    Song Data Model Schema

    """

    class Meta:
        fields = ("id", "name", "duration", "uploaded_time")


class PodcastSchema(ma.Schema):
    """
    Podcast Data Model Schema

    """

    class Meta:
        fields = ("id", "name", "duration", "uploaded_time", "host", "participants")


class AudioBookSchema(ma.Schema):
    """
    Audiobook Data Model Schema

    """

    class Meta:
        fields = ("id", "name", "author", "narrator", "duration", "uploaded_time")
