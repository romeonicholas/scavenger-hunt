from flask import Blueprint, render_template
from .models import Greeting
from app.scripts.db_utils import get_random_greeting

blueprint = Blueprint("greetings", __name__, url_prefix="/greetings")


@blueprint.get("/")
def index():
    try:
        greetings = Greeting.query.all()
        return render_template("greetings/show.html", greetings=greetings)
    except Exception as e:
        print(e)  # move to log, display error in template
        return render_template("greetings/show.html", greetings=[])


@blueprint.get("/random")
def random():
    try:
        random_greeting = get_random_greeting()
        return render_template("greetings/random.html", random_greeting=random_greeting)
    except Exception as e:
        print(e)  # move to log, display error in template
        random_greeting = {"english_text": "Hello!"}
        return render_template("greetings/random.html", random_greeting=random_greeting)
