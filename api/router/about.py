from flask import Blueprint, jsonify

app = Blueprint('about', __name__, template_folder='../templates')

@app.route("/about", methods=['GET'])
def hello_about():
    return jsonify(code=200, data='this is about page')