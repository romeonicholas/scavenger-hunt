from app.extensions.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)

    # to be implemented:
    # avatar
    # color
    # current game
    # current step
    # answered questions
