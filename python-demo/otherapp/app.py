from flask import Flask
from .router.index import bp_index
from .router.about import bp_about

app = Flask(__name__)

app.jinja_env.auto_reload = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.register_blueprint(bp_index)
app.register_blueprint(bp_about)
