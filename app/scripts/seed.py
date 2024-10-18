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
    {
        "english_text": "Hello",
        "indiginous_text": "ᏂꮒᎦꭶ",
        "language": "English",
        "tribe": "america",
    },
    {
        "english_text": "Hi",
        "indiginous_text": "Hoo",
        "language": "abc",
        "tribe": "cherokee",
    },
    {
        "english_text": "G'day",
        "indiginous_text": "Haa",
        "language": "def",
        "tribe": "osage",
    },
    {
        "english_text": "Greetings",
        "indiginous_text": "Heee",
        "language": "ghi",
        "tribe": "hawk",
    },
]

for greeting in greetings:
    db.session.add(Greeting(**greeting))

db.session.commit()
