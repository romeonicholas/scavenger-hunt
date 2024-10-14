from flask import Flask
from . import simple_pages, users

app = Flask(__name__)
app.config.from_object("app.config")

app.register_blueprint(users.routes.blueprint)
app.register_blueprint(simple_pages.routes.blueprint)

# game in progress page
# looks for session in progress based on user, displays current step
