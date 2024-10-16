from flask import Blueprint, render_template

blueprint = Blueprint("greetings", __name__, url_prefix="/greetings")


@blueprint.get("/")
def index():
    return render_template("greetings/show.html")
