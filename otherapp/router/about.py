from flask import Blueprint

app = Blueprint('about', __name__, template_folder='../templates')

@app.route("/about")
def hello_about():
    return "<p>Hello, World! This is About!</p>"