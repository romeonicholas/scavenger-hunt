from app.extensions.database import db


class Greeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(16), unique=True)
