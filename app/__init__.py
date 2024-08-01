from flask import Flask, render_template
from .router.index import app as index
from .router.add import app as add
from .router.upload import app as upload

app = Flask(__name__)

app.jinja_env.auto_reload = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

# 当前项目文件夹
app.config["ROOT_DIR"] = "app"


app.register_blueprint(index)
app.register_blueprint(add)
app.register_blueprint(upload)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.twig", error=error)
