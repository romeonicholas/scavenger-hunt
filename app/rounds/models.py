from app.extensions.database import db


class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
