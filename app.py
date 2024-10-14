from flask import Flask

app = Flask(__name__)
app.config.from_object("config")


# first view
# returns to this on timeout/logout
# containd dynamic "hello" from db
@app.route("/")
def index():
    return "Welcome to the scavenger hunt!"


# new player page
# multi-step form for name, avatar, and confirmation/welcom
@app.route("/users/new", methods=["GET"])
def get_new_user():
    return "New user form"


# create new player from form
@app.route("/users/new", methods=["POST"])
def post_new_user():
    return "New user created, redirected to game"


# continuing player page
# displays all/most recent player badges(name, avatar, color)
@app.route("/users")
def get_users():
    return "Existing users page"


# game in progress page
# looks for session in progress based on user, displays current step
if __name__ == "__main__":
    app.run()
