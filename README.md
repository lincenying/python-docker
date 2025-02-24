# JavaScript Ajax Example

演示如何使用 JavaScript 发布表单数据并处理 JSON 响应。这样无需离开页面即可发出请求。
演示如何使用 [fetch](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch)、[XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) 和[jQuery.ajax](https://api.jquery.com/jQuery.ajax/)。
有关 JavaScript 和 Ajax，请参阅 [Flask 文档](https://flask.palletsprojects.com/patterns/javascript/)。

## Install

```bash
# 创建虚拟环境
python3 -m venv .venv
# 激活虚拟环境
# linux/mac
. .venv/bin/activate
# win
.venv/Scripts/activate
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

如果使用宿主机起`mongodb`服务, 可以直接使用下面命令构建启动容器
如果要将`mongodb`也容器化, 可以直接使用`docker-compose`

```bash
# 构建镜像
docker build -t images-python-demo -f ./Dockerfile .
# 运行镜像, 映射本地数据库路径到容器中
docker run -d \
-p 8006:8006 -p 8007:8007 -p 8008:8008 \
-e MONGO_URI=mongodb://host.docker.internal:27017 \
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

修改`docker-compose.yml`中的`volumes`配置, 将宿主机数据库路径映射到容器中

```yaml
volumes:
    - /Users/lincenying/web/mongodb/data:/data/db
```

```bash
docker-compose up -d
```
