from flask import Flask

app = Flask(__name__)
app.config.from_object("config")


@app.route("/")
def index():
    return "Welcome to the scavenger hunt!"


if __name__ == "__main__":
    app.run()
