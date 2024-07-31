from flask import Flask
from .router.index import app as index
from .router.about import app as about

app = Flask(__name__)

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.register_blueprint(index)
app.register_blueprint(about)