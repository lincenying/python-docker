from flask import Flask, jsonify, request
from .router.index import bp_index
from .router.about import bp_about

app = Flask(__name__)

app.jinja_env.auto_reload = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.register_blueprint(bp_index, url_prefix="/api")
app.register_blueprint(bp_about, url_prefix="/api")


@app.errorhandler(404)
def page_not_found(error):
    return jsonify(code=404, data=None, err=str(error))
