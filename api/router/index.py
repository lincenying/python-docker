from flask import Blueprint, jsonify

bp_index = Blueprint("index", __name__, template_folder="../templates")


@bp_index.route("/index", methods=["GET"])
def hello_world():
    return jsonify(code=200, data="this is index page")
