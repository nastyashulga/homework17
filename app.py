# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.directors import directors_ns
from views.genres import genres_ns
from views.movies import movies_ns


#функция создания основного объекта app
def create_app(config: Config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()

    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def configure_app(app):
    db.init_app(app)
    db.create_all()
    api = Api(app, prefix='/')
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)

    configure_app(app)
    app.run(host="localhost", port=10071)
