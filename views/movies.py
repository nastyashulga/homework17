from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movie import MovieSchema

movies_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movies_ns.route('/')
class MoviesView(Resource):

    def get(self):
        movies = movie_service.get_all()

        return movies_schema.dump(movies), 200

    def post(self):
        req_json = request.json
        movie = movie_service.create(req_json)
        return "", 201


@movies_ns.route('/<int:mid>')
class MoviesView(Resource):

    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        movie = movie_service.get_one(mid)
        movie_service.update(movie)
        return "", 204


    def delete(self, mid):
        movie_service.delete(mid)
        return "", 204


@movies_ns.route('/<int:director_id>')
class MoviesView(Resource):

    def get(self, director_id):
        directors = movie_service.get_by_director(director_id)
        return movies_schema.dump(directors), 200

@movies_ns.route('/<int:genre_id>')
class MoviesView(Resource):

    def get(self, genre_id):
        genres = movie_service.get_by_genre(genre_id)
        return movies_schema.dump(genres), 200

@movies_ns.route('/<int:year>')
class MoviesView(Resource):

    def get(self, year):
        years = movie_service.get_by_year(year)
        return movies_schema.dump(years), 200