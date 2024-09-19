from math import ceil
from bson import ObjectId
from flask import Blueprint, jsonify, request

from app.mongo import mongo

bp_article = Blueprint("article", __name__, url_prefix="/article")


@bp_article.route("/lists", methods=["POST", "GET"])
def lists():
    articles_db = mongo.db.articles  # type: ignore

    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))

    if page < 1:
        page = 1
    if per_page < 1:
        per_page = 10

    # 计算偏移量
    offset = (page - 1) * per_page

    article_list = []
    total = 0
    total_page = 1

    articles = (
        articles_db.find({"is_delete": 0}, {"content": False})
        .skip(offset)
        .limit(per_page)
        .sort("update_date", -1)
    )

    # 将结果转换为列表
    article_list = list(articles)

    total = articles_db.count_documents({})
    total_page = ceil(total / per_page)

    # 返回 JSON 响应
    return jsonify(
        {
            "code": 200,
            "message": "查询成功",
            "lists": {
                "page": page,
                "per_page": per_page,
                "total": total,
                "total_page": total_page,
                "data": article_list,
            },
        }
    )


@bp_article.route("/item", methods=["POST", "GET"])
def item():
    articles_db = mongo.db.articles  # type: ignore

    id = request.args.get("id")
    if id is None:
        return jsonify({"code": 404, "message": "ID不能为空!", "data": None})

    article = articles_db.find_one({"_id": ObjectId(id), "is_delete": 0})

    if article is None:
        return jsonify({"code": 404, "message": "文章不存在!", "data": None})

    return jsonify(
        {
            "code": 200,
            "message": "success",
            "data": article,
        }
    )


@bp_article.route("/trending", methods=["POST", "GET"])
def trending():
    articles_db = mongo.db.articles  # type: ignore

    articles = (
        articles_db.find({"is_delete": 0}, {"content": False})
        .limit(5)
        .sort("visit", -1)
    )
    article_list = list(articles)

    return jsonify(
        {
            "code": 200,
            "message": "success",
            "data": article_list,
        }
    )
