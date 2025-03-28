from flask import Blueprint, render_template

from app.mongo import mongo

bp_index = Blueprint("index", __name__, template_folder="../templates")


@bp_index.route("/", defaults={"page": "fetch"})
@bp_index.route("/<any(xhr, jquery, fetch):page>")
def index(page: str):
    admins_db = mongo.db.admins  # type: ignore

    users = []
    if mongo.db is not None:
        users = list(admins_db.find({}))
    return render_template(f"{page}.twig", page=page, users=users)
