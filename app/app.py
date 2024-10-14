from flask import Flask
from . import simple_pages, users


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config")

    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(users.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)


# game in progress page
# looks for session in progress based on user, displays current step
