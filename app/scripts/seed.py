from app.app import create_app
from app.users.models import User
from app.greetings.models import Greeting
from app.riddles.models import Riddle, Answer, RiddleAnswer
from app.extensions.database import db

if __name__ == "__main__":
    app = create_app()
    app.app_context().push()

### USERS ###

users = [
    {"name": "Alice"},
    {"name": "Bob"},
    {"name": "Charlie"},
    {"name": "David"},
    {"name": "Eve"},
]

for user in users:
    db.session.add(User(**user))

### GREETINGS ###

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

### RIDDLES & ANSWERS ###

riddle = Riddle(
    clue_1="Everyone knows I'm great:\nI'm the official wildflower of our state!",
    clue_2="You might see me near a star of blue,\nor the tail of a cat, at that!",
    clue_3="Are you still looking for more?\nTry next to the rabbit, out the front door.",
    question="Who am I?",
)

answer1 = Answer(text="Indian Blanket", image="flower_blue.jpeg")
answer2 = Answer(text="False Dandelion", image="flower_yellow.jpeg")
answer3 = Answer(text="Coreopsis", image="flower_red.jpeg")
answer4 = Answer(text="Purple Cornflower", image="flower_green.jpeg")

riddle_answer1 = RiddleAnswer(riddle=riddle, answer=answer1, is_correct=True)
riddle_answer2 = RiddleAnswer(riddle=riddle, answer=answer2, is_correct=False)
riddle_answer3 = RiddleAnswer(riddle=riddle, answer=answer3, is_correct=False)
riddle_answer4 = RiddleAnswer(riddle=riddle, answer=answer4, is_correct=False)

db.session.add(riddle)
db.session.add(answer1)
db.session.add(answer2)
db.session.add(answer3)
db.session.add(answer4)
db.session.add(riddle_answer1)
db.session.add(riddle_answer2)
db.session.add(riddle_answer3)
db.session.add(riddle_answer4)

db.session.commit()
