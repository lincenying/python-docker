# 使用官方的Python基础镜像
FROM python:3.9-slim-buster
LABEL maintainer="LinCenYing lincenying@gmail.com"
# 升级pip版本
RUN pip install --upgrade pip
# 复制应用代码到容器
COPY . /app
# 设置工作目录
WORKDIR /app
# 镜像源地址为npmmirror镜像源, 镜像源地址为https://registry.npmmirror.com/-/binary/python, 镜像源地址跳过校验
# 镜像源地址为https://registry.npmmirror.com/-/binary/python, 镜像源地址跳过校验
RUN export PYTHON_BUILD_MIRROR_URL="https://registry.npmmirror.com/-/binary/python"
RUN export PYTHON_BUILD_MIRROR_URL_SKIP_CHECKSUM=1
# 安装应用的依赖
RUN pip3 install -e .

# 设置环境变量
ENV FLASK_APP1=app:app

## 生产环境
ENV NODE_ENV=production
## 如果没有将mongodb容器化, name数据库地址为宿主机数据库地址
ENV MONGO_URI=mongodb://host.docker.internal:27017

# 暴露端口
EXPOSE 8007
# 运行Gunicorn服务
CMD ["sh", "-c", "gunicorn -w 2 -b 0.0.0.0:8007 --timeout 90 $FLASK_APP1"]
