# JavaScript Ajax Example

演示如何使用 JavaScript 发布表单数据并处理 JSON 响应。这样无需离开页面即可发出请求。
演示如何使用 [fetch](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch)、[XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) 和[jQuery.ajax](https://api.jquery.com/jQuery.ajax/)。
有关 JavaScript 和 Ajax，请参阅 [Flask 文档](https://flask.palletsprojects.com/patterns/javascript/)。

## Install

```bash
# 创建虚拟环境
python3 -m venv .venv
# 激活虚拟环境
. .venv/bin/activate
# 升级pip
pip install --upgrade pip
# 安装依赖
pip3 install -e .
```

## Run

```bash
flask --app app run --debug
```

```bash
flask --app otherapp.app run --debug --port 5001
```

```bash
flask --app api.app run --debug --port 5002
```

Open <http://127.0.0.1:5000> in a browser.

## Prod

```bash
pip install gunicorn
gunicorn -w 4 -b 127.0.0.1:8001 app:app
gunicorn -w 4 -b 127.0.0.1:8002 otherapp.app:app
gunicorn -w 4 -b 127.0.0.1:8003 api.app:app
# gunicorn -w 4 -b 127.0.0.1:端口 入口文件:实例
```

## Test

```bash
pip install -e '.[test]'
coverage run -m pytest
coverage report
```

## docker

```bash
# 构建镜像
docker build -t images-python-demo -f ./Dockerfile .
# 运行镜像, 映射本地数据库路径到容器中
docker run -d \
-p 8006:8006 -p 8007:8007 -p 8008:8008 \
--name container-python-demo \
images-python-demo
# 进入镜像
docker exec -it container-python-demo /bin/bash
# 停止容器
docker stop container-python-demo
# 删除容器
docker rm container-python-demo
# 删除镜像
docker rmi images-python-demo
```

## docker-compose

```bash
docker-compose up -d
```
