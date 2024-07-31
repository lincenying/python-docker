from flask import Flask, render_template

app = Flask(__name__)

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

from .router.index import app as index
from .router.add import app as add

app.register_blueprint(index)
app.register_blueprint(add)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.twig')