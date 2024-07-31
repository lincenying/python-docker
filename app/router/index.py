from flask import Blueprint, render_template

app = Blueprint('index', __name__, template_folder='../templates')

@app.route("/", defaults={"page": "fetch"})
@app.route("/<any(xhr, jquery, fetch):page>")
def index(page):
    return render_template(f"{page}.twig", page=page)