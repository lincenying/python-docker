from flask import Blueprint, jsonify

bp_about = Blueprint("about", __name__, template_folder="../templates")


@bp_about.route("/about", methods=["GET"])
def hello_about():
    return jsonify(code=200, data="this is about page")
