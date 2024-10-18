from sqlalchemy.sql import func
from .models import Riddle, RiddleAnswer


def get_riddle(riddle_id):
    return Riddle.query.get(riddle_id)


def get_all_riddles():
    return Riddle.query.all()


def get_answers(riddle_id):
    riddle_answers = RiddleAnswer.query.filter_by(riddle_id=riddle_id).all()
    return [
        {
            "text": ra.answer.text,
            "image": ra.answer.image,
            "is_correct": ra.is_correct,
        }
        for ra in riddle_answers
    ]
