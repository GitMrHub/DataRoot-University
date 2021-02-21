from datetime import datetime as dt

from core import db
from .base import Model
from .relations import association


class Movie(Model, db.Model):
    __tablename__ = 'movies'

    # id -> integer, primary key
    id = db.Column(db.Integer, primary_key = True)
    # name -> string, size 50, unique, not nullable
    name =  db.Column(db.String(50), unique = True, nullable = False)
    # year -> integer
    year = db.Column(db.Integer)
    # genre -> string, size 20
    genre = db.Column(db.String(20))

    # Use `db.relationship` method to define the Movie's relationship with Actor.
    # Set `backref` as 'filmography', uselist=True
    # Set `secondary` as 'association'
    actors = db.relationship('Actor', backref='filmography', uselist=True, secondary='association')

    def __repr__(self):
        return '<Movie {}>'.format(self.name)