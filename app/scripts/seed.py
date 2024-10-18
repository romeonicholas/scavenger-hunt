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

db.session.commit()

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

db.session.commit()

### RIDDLES & ANSWERS ###

riddles_data = [
    {
        "riddle": {
            "clue_1": "Everyone knows I'm great:\nI'm the official wildflower of our state!",
            "clue_2": "You might see me near a star of blue,\nor the tail of a cat, at that!",
            "clue_3": "Are you still looking for more?\nTry next to the rabbit, out the front door.",
            "question": "Who am I?",
        },
        "answers": [
            {"text": "Indian Blanket", "image": "flower_blue.jpeg", "is_correct": True},
            {
                "text": "False Dandelion",
                "image": "flower_yellow.jpeg",
                "is_correct": False,
            },
            {"text": "Coreopsis", "image": "flower_red.jpeg", "is_correct": False},
            {
                "text": "Purple Cornflower",
                "image": "flower_green.jpeg",
                "is_correct": False,
            },
        ],
    },
    {
        "riddle": {
            "clue_1": "Painted Bunting is my name,\nColorful feathers are my fame!",
            "clue_2": "I'm divided by four distinct hues:\nYellow, red, green, and blue.",
            "clue_3": "Usually I try to hide from y'all\nBut today I'm out near the waterfall!",
            "question": "What color is my head?",
        },
        "answers": [
            {"text": "Blue", "image": "flower_blue.jpeg", "is_correct": False},
            {"text": "Red", "image": "flower_yellow.jpeg", "is_correct": False},
            {"text": "Green", "image": "flower_red.jpeg", "is_correct": True},
            {"text": "Yellow", "image": "flower_green.jpeg", "is_correct": False},
        ],
    },
    {
        "riddle": {
            "clue_1": "What, haven't you heard?\nI'm the Oklahoma state bird.",
            "clue_2": "Right now you'll find me flying high:\nAbove the herd, up in the sky.",
            "clue_3": "I see a scary snake close to here,\nAnd also … is that a baby blue deer?",
            "question": "Who am I?",
        },
        "answers": [
            {
                "text": "Red-tailed Hawk",
                "image": "flower_blue.jpeg",
                "is_correct": False,
            },
            {
                "text": "Ruby-throated Hummingbird",
                "image": "flower_yellow.jpeg",
                "is_correct": False,
            },
            {
                "text": "Scissor-tailed Flycatcher",
                "image": "flower_red.jpeg",
                "is_correct": False,
            },
            {
                "text": "Prairie Falcon",
                "image": "flower_green.jpeg",
                "is_correct": True,
            },
        ],
    },
    {
        "riddle": {
            "clue_1": "You'll find me in the scrub to the East,\nhunting for a termite feast.",
            "clue_2": "Unlike two critters that are near me,\nI have no quills or feathers, you'll see.",
            "clue_3": "I'm out in the sun on a big red ledge,\nmaybe standing too close to the edge?",
            "question": "Who am I?",
        },
        "answers": [
            {"text": "Armadillo", "image": "flower_blue.jpeg", "is_correct": False},
            {
                "text": "Swift Fox",
                "image": "flower_yellow.jpeg",
                "is_correct": True,
            },
            {"text": "Prairie Dog", "image": "flower_red.jpeg", "is_correct": False},
            {
                "text": "Porcupine",
                "image": "flower_green.jpeg",
                "is_correct": False,
            },
        ],
    },
]

for riddle_data in riddles_data:
    riddle_info = riddle_data["riddle"]
    answers_info = riddle_data["answers"]

    riddle = Riddle(
        clue_1=riddle_info["clue_1"],
        clue_2=riddle_info["clue_2"],
        clue_3=riddle_info["clue_3"],
        question=riddle_info["question"],
    )

    db.session.add(riddle)
    db.session.commit()

    for answer_info in answers_info:
        answer = Answer(text=answer_info["text"], image=answer_info["image"])
        db.session.add(answer)
        db.session.commit()

        riddle_answer = RiddleAnswer(
            riddle_id=riddle.id,
            answer_id=answer.id,
            is_correct=answer_info["is_correct"],
        )
        db.session.add(riddle_answer)

db.session.commit()
