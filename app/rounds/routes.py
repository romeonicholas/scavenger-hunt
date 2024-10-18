from flask import Blueprint, render_template

blueprint = Blueprint(
    "rounds",
    __name__,
)


@blueprint.get("/rounds")
def index():
    try:
        # query rounds
        return render_template("rounds/show.html", rounds=[])
    except Exception as e:
        print(e)  # move to log, display error in template
        return render_template("rounds/show.html", rounds=[])
