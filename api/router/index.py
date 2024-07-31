from flask import Blueprint, jsonify

app = Blueprint("index", __name__, template_folder="../templates")


@app.route("/index", methods=["GET"])
def hello_world():
    return jsonify(code=200, data="this is index page")
