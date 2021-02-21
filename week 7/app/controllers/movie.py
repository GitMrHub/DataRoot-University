from flask import jsonify, make_response

from ast import literal_eval

from models import Movie, Actor
from settings.constants import MOVIE_FIELDS
from .parse_request import get_request_data


def get_all_movies():
    """
    Get list of all records
    """
    all_movies = Movie.query.all()
    movies = []
    for movie in all_movies:
        mov = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
        movies.append(mov)
    return make_response(jsonify(movies), 200)


def get_movie_by_id():
    """
    Get record by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        obj = Movie.query.filter_by(id=row_id).first()
        try:
            movie = {k: v for k, v in obj.__dict__.items() if k in MOVIE_FIELDS}
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        return make_response(jsonify(movie), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)

def add_movie():
    """
    Add new movie
    """
    data = get_request_data()
    new_record = Movie.create(**data)
    new_movie = {k: v for k, v in new_record.__dict__.items() if k in MOVIE_FIELDS}
    return make_response(jsonify(new_movie), 200)

def update_movie():
    """
    Update movie record by id
    """
    data = get_request_data()

    upd_record = Movie.update(**data)
    upd_movie = {k: v for k, v in upd_record.__dict__.items() if k in MOVIE_FIELDS}
    return make_response(jsonify(upd_movie), 200)

def delete_movie():
    """
    Delete movie by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)
        if Movie.delete(row_id):
            msg = 'Record successfully deleted'
            return make_response(jsonify(message=msg), 200)
        else:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)

def movie_add_relation():
    """
    Add actor to movie's cast
    """
    data = get_request_data()
    obj = Actor.query.filter_by(id=data['relation_id']).first()
    movie = Movie.add_relation(data['id'], obj)
    rel_movie = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
    rel_movie['filmography'] = str(movie.cast)
    return make_response(jsonify(rel_movie), 200)
    # if 'id' in data.keys() and 'relation_id' in data.keys():
    #     try:
    #         movie = Movie.add_relation(data['id'], data['relation_id'])
    #         rel_movie = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
    #         rel_movie['cast'] = str(movie.cast)
    #         return make_response(jsonify(rel_movie), 200)
    #     except:
    #         err = 'Record with such id and relation_id does not exist'
    #         return make_response(jsonify(error=err), 400)
    # else:
    #     err = 'Id or relation_id not specified'
    #     return make_response(jsonify(error=err), 400)

def movie_clear_relations():
    """
    Clear all relations by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)
        try:
            movie =  Movie.query.filter_by(id=row_id).first()  # clear relations here
            rel_movie = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
            rel_movie['cast'] = str(movie.cast)
            return make_response(jsonify(rel_movie), 200)
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'Id not specified'
        return make_response(jsonify(error=err), 400)