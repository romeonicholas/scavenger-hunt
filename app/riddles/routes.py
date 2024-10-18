from flask import Blueprint, render_template
from .models import Riddle, Answer, RiddleAnswer

blueprint = Blueprint(
    "riddles",
    __name__,
)


@blueprint.get("/riddles")
def index():
    try:
        # riddles = Riddle.query.all()
        return render_template("riddles/index.html", riddles=[])
    except Exception as e:
        print(e)  # move to log, display error in template
        return render_template("riddles/index.html", riddles=[])


@blueprint.get("/riddles/<int:riddle_id>")
def show(riddle_id):
    try:
        riddle = Riddle.query.get(riddle_id)
        print(riddle)
        riddle_answers = RiddleAnswer.query.filter_by(riddle_id=riddle_id).all()
        print(riddle_answers)
        return render_template(
            "riddles/show.html", riddle=riddle, riddle_answers=riddle_answers
        )
    except Exception as e:
        print(e)
