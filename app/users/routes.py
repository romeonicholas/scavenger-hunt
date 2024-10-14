from flask import Blueprint, render_template

blueprint = Blueprint("users", __name__, url_prefix="/users")


# continuing player page
# displays all/most recent player badges(name, avatar, color)
@blueprint.get("/")
def get_users():
    return render_template("users/show.html")


# new player page
# multi-step form for name, avatar, and confirmation/welcom
@blueprint.get("/new")
def get_new_user():
    return render_template("users/new.html")


# create new player from form
@blueprint.post("/new")
def post_new_user():
    return "New user created, redirected to game"
