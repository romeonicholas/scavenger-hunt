from sqlalchemy.sql import func
from app.greetings.models import Greeting


def get_random_greeting():
    # pylint: disable=not-callable
    return Greeting.query.order_by(func.random()).first()
