from flask import Blueprint, render_template

blueprint = Blueprint("simple_pages", __name__)


# first view
# returns to this on timeout/logout
# contains dynamic "hello" from db
@blueprint.get("/")
def index():
    return render_template("simple_pages/index.html")
