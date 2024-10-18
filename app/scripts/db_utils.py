from app.greetings.models import Greeting
from sqlalchemy.sql import func


def get_random_greeting():
    return Greeting.query.order_by(func.random()).first()
