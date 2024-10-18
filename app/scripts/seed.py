from app.app import create_app
from app.users.models import User
from app.greetings.models import Greeting
from app.extensions.database import db

if __name__ == "__main__":
    app = create_app()
    app.app_context().push()

users = [
    {"name": "Alice"},
    {"name": "Bob"},
    {"name": "Charlie"},
    {"name": "David"},
    {"name": "Eve"},
]

for user in users:
    db.session.add(User(**user))


greetings = [
    {"english_text": "066"},
    {"english_text": "Hi"},
    {"english_text": "Hey"},
    {"english_text": "Yo"},
    {"english_text": "Greetings"},
]

for greeting in greetings:
    db.session.add(Greeting(**greeting))

db.session.commit()
