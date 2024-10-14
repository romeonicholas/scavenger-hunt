from flask import Flask, render_template
from . import users

app = Flask(__name__)
app.config.from_object("app.config")

app.register_blueprint(users.routes.blueprint)


# first view
# returns to this on timeout/logout
# contains dynamic "hello" from db
@app.route("/")
def index():
    return render_template("index.html")


# game in progress page
# looks for session in progress based on user, displays current step
