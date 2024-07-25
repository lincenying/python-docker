from flask import Flask

app2 = Flask(__name__)

app2.jinja_env.auto_reload = True

app2.config['TEMPLATES_AUTO_RELOAD'] = True

@app2.route("/")
def hello_world():
    return "<p>Hello, World!</p>"