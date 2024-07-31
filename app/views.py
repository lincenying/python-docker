import json
import time
from flask import jsonify, render_template, request

from . import app


@app.route("/", defaults={"js": "fetch"})
@app.route("/<any(xhr, jquery, fetch):js>")
def index(js):
    return render_template(f"{js}.twig", js=js)


@app.route("/add/form", methods=["POST"])
def addform():
    a = request.form.get("a", 0, type=float)
    b = request.form.get("b", 0, type=float)
    return jsonify(code=200, result=a + b)

@app.route("/add/json", methods=["POST"])
def addjson():
    print("content_type:", request.headers.get("content_type"))
    print(request.json)
    print(request.form)
    print(request.data)
    print(type(request.json))
    print(type(request.form))
    print(type(request.data))
    print(request.data.decode())
    print(type(request.data.decode()))
    c = {}
    try:
        c = json.loads(request.data.decode())
    except:
        print('err')
    print(c)
    a = float(request.json['a'])
    b = float(request.json['b'])
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    
    d = {}
    try:
        d = json.loads('{a}')
    except:
        print('err')
    print(d)
    
    return jsonify(code=200, result=a + b)

@app.route("/add/query", methods=["GET"])
def addquery():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify(code=200, result=a + b)



# request.args.get('name')  # GET
# request.form.get('name')  # POST
# request.values.get('name')  # GET, POST
# request.cookies.get('name')  # cookie
# request.headers.get("content_type") # header
# request.files.get('name')  # file
# request.json  # json
# request.method  # method
# request.url  # url
# request.path  # path
# request.full_path  # full_path