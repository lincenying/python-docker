import os
from flask import Flask, render_template
from .mongo import mongo

from .router.index import bp_index
from .router.add import bp_add
from .router.upload import bp_upload

app = Flask(__name__)

MONGO_URI = os.environ.get("MONGO_URI") or "mongodb://localhost:27017"

app.config["MONGO_URI"] = MONGO_URI + "/mmfblog_v2"
mongo.init_app(app)

app.jinja_env.auto_reload = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.register_blueprint(bp_index)
app.register_blueprint(bp_add)
app.register_blueprint(bp_upload)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.twig", error=error)
