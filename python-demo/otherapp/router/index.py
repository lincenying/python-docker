from flask import Blueprint

bp_index = Blueprint("index", __name__, template_folder="../templates")


@bp_index.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
