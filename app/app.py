from flask import Flask
from app.extensions.database import db, migrate
from . import simple_pages, users, greetings, rounds, riddles


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config")
    app.url_map.strict_slashes = False

    register_extensions(app)
    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(users.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)
    app.register_blueprint(greetings.routes.blueprint)
    app.register_blueprint(rounds.routes.blueprint)
    app.register_blueprint(riddles.routes.blueprint)


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
