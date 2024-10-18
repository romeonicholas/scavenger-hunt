from app.extensions.database import db


class Greeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    english_text = db.Column(db.String(16))
