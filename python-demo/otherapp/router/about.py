from flask import Blueprint

bp_about = Blueprint("about", __name__, template_folder="../templates")


@bp_about.route("/about")
def hello_about():
    return "<p>Hello, World! This is About!</p>"
