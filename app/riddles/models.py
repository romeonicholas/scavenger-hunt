from app.extensions.database import db


class Riddle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clue_1 = db.Column(db.String(64))
    clue_2 = db.Column(db.String(64))
    clue_3 = db.Column(db.String(64))
    question = db.Column(db.String(64))

    answers = db.relationship("RiddleAnswer", back_populates="riddle")


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(64))
    image = db.Column(db.String(64))

    riddles = db.relationship("RiddleAnswer", back_populates="answer")


class RiddleAnswer(db.Model):
    __tablename__ = "riddle_answer"
    id = db.Column(db.Integer, primary_key=True)
    riddle_id = db.Column(db.Integer, db.ForeignKey("riddle.id"))
    answer_id = db.Column(db.Integer, db.ForeignKey("answer.id"))
    is_correct = db.Column(db.Boolean, default=False)

    riddle = db.relationship("Riddle", back_populates="answers")
    answer = db.relationship("Answer", back_populates="riddles")
