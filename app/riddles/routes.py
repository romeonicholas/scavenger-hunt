from flask import Blueprint, render_template

blueprint = Blueprint(
    "riddles",
    __name__,
)


@blueprint.get("/riddles")
def index():
    try:
        # riddles = Riddle.query.all()
        return render_template("riddles/show.html", riddles=[])
    except Exception as e:
        print(e)  # move to log, display error in template
        return render_template("riddles/show.html", riddles=[])
