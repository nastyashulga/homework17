# файл для создания DAO и сервисов чтобы импортировать их везде
from dao.movie import MovieDAO
from dao.genre import GenreDAO
from dao.director import DirectorDAO
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from setup_db import db


movie_dao = MovieDAO(db.session)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

movie_service = MovieService(movie_dao, genre_dao, director_dao)
