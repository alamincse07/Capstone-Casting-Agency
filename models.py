
from sqlalchemy import Table, Column, Float, Integer, String, MetaData, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os
from flask_migrate import Migrate

# TODO: enable this line
database_path = os.environ['DATABASE_URL']

#database_path = 'postgresql://postgres:root@localhost:5432/movie-agency'
db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    db.create_all()


def db_drop_and_create_all():
    pass


linking_table = Table('linking_table', db.Model.metadata, Column('movie_id', Integer, ForeignKey('movies.id')), Column('actor_id', Integer, ForeignKey('actors.id')))

class Actor(db.Model):

    __tablename__ = "actors"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    gender = Column(String(6), nullable=False)
    movies = db.relationship('Movie', secondary=linking_table,
                             backref='actor_list', lazy=True)

    def insert(self):

        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'movies': []
        }


class Movie(db.Model):

    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String(120), unique=True, nullable=False)
    release_date = Column(String(120), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    def format(self):

        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
        }


