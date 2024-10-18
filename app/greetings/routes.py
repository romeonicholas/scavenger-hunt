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
        random_greeting_text = get_random_greeting().text
        return render_template(
            "greetings/random.html", random_greeting_text=random_greeting_text
        )
    except Exception as e:
        print(e)  # move to log, display error in template
        return render_template("greetings/random.html", random_greeting_text="Hello!")
