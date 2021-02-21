from flask import Flask, request
from flask import current_app as app

from controllers.actor import *
from controllers.movie import *


@app.route('/api/actors', methods=['GET'])
def actors():
    """
    Get all actors in db
    """
    return get_all_actors()

@app.route('/api/movies', methods=['GET'])
def movies():
    """
    Get all movies in db
    """
    return get_all_movies()

@app.route('/api/actor', methods=['GET', 'POST', 'PUT', 'DELETE'])
def actor():
    if request.method == 'GET':
        return get_actor_by_id()
    elif request.method == 'POST':
        return add_actor()
    elif request.method == 'PUT':
        return update_actor()
    elif request.method == 'DELETE':
        return delete_actor()

@app.route('/api/movie', methods=['GET', 'POST', 'PUT', 'DELETE'])
def movie():
    if request.method == 'GET':
        return get_movie_by_id()
    elif request.method == 'POST':
        return add_movie()
    elif request.method == 'PUT':
        return update_movie()
    elif request.method == 'DELETE':
        return delete_movie()

@app.route('/api/actor-relations', methods=['PUT', 'DELETE'])
def actor_relation():
    """
    Get all movies in db
    """
    if request.method == 'PUT':
        return actor_add_relation()
    elif request.method == 'DELETE':
        return actor_clear_relations()

@app.route('/api/movie-relations', methods=['PUT', 'DELETE'])
def movie_relation():
    """
    Get all movies in db
    """
    if request.method == 'PUT':
        return movie_add_relation()
    elif request.method == 'DELETE':
        return movie_clear_relations()

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime as dt
#
# from settings.constants import DB_URL
# from core import db
# from models.actor import Actor
# from models.movie import Movie
#
#
# app = Flask(__name__, instance_relative_config=False)
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # silence the deprecation warning
#
# db.init_app(app)

# data_actor = {'name': 'Megan Fox', 'gender': 'female', 'date_of_birth': dt.strptime('16.05.1986', '%d.%m.%Y').date()}
# data_actor_upd = {'name': 'Not Megan Fox', 'gender': 'male', 'date_of_birth': dt.strptime('16.05.2000', '%d.%m.%Y').date()}
#
# data_movie = {'name': 'Transformers', 'genre': 'action', 'year': 2007}
# data_movie_upd = {'name': 'Teenage Mutant Ninja Turtles', 'genre': 'bad movie', 'year': 2014}
#
# app = Flask(__name__, instance_relative_config=False)
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # silence the deprecation warning
#
# db.init_app(app)
#
# with app.app_context():
#     db.drop_all()
#     db.create_all()
#     actor = Actor.create(**data_actor)
#     print('created actor:', actor.__dict__, '\n')
#
#     movie = Movie.create(**data_movie)
#     print('created movie:', movie.__dict__, '\n')
#
#     upd_actor = Actor.update(1, **data_actor_upd)
#     print('updated actor:', upd_actor.__dict__, '\n')
#
#     upd_movie = Movie.update(1, **data_movie_upd)
#     print('updated movie:', upd_movie.__dict__, '\n')
#
#     add_rels_actor = Actor.add_relation(1, upd_movie)
#     movie_2 = Movie.create(**data_movie)
#     add_more_rels_actor = Actor.add_relation(1, movie_2)
#     print('relations list:', add_more_rels_actor.filmography, '\n')
#
#     clear_rels_actor = Actor.clear_relations(1)
#     print('all relations cleared:', clear_rels_actor.filmography, '\n')
#
#     del_actor = Actor.delete(1)
#     print('actor deleted:', del_actor)