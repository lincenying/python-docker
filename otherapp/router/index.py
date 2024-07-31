from flask import Blueprint

app = Blueprint("index", __name__, template_folder="../templates")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
