from flask import Flask, render_template
import os
from flask_pymongo import PyMongo
from flask.json.provider import DefaultJSONProvider
from bson import ObjectId
from datetime import datetime

from app.mongo import mongo

from .router.index import bp_index
from .router.add import bp_add
from .router.upload import bp_upload
from .router.article import bp_article


class MongoJSONProvider(DefaultJSONProvider):
    def default(self, obj):  # type: ignore
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)


app = Flask(__name__)

app.json = MongoJSONProvider(app)
MONGO_URI = (
    os.environ.get("DATABASE_URL")
    or os.environ.get("MONGO_URI")
    or "mongodb://localhost:27017"
)
# 设置默认的JSON提供者在处理数据时保留原始字符编码，不转换为ASCII码
DefaultJSONProvider.ensure_ascii = False
app.config["MONGO_URI"] = MONGO_URI + "/mmfblog_v2"
mongo.init_app(app)

app.jinja_env.auto_reload = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.register_blueprint(bp_index)
app.register_blueprint(bp_add)
app.register_blueprint(bp_upload)
app.register_blueprint(bp_article)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.twig", error=error)
