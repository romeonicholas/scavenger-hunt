from flask import Blueprint, render_template
from .db_utils import get_riddle, get_answers


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
        riddle = get_riddle(riddle_id)
        answers = get_answers(riddle_id)

        return render_template("riddles/show.html", riddle=riddle, answers=answers)
    except Exception as e:
        print(e)
