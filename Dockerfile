# 使用官方的Python基础镜像
FROM python:3.9`
LABEL maintainer="LinCenYing lincenying@gmail.com"
# 升级pip版本
RUN pip install --upgrade pip
# 复制应用代码到容器
COPY . /app
# 设置工作目录
WORKDIR /app
# 安装应用的依赖
RUN pip3 install -e .

# 设置环境变量
ENV FLASK_APP1=app:app
ENV FLASK_APP2=otherapp.app:app
ENV FLASK_APP3=api.app:app

# 暴露端口
EXPOSE 8006 8007 8008
# 运行Gunicorn服务
CMD ["sh", "-c", "gunicorn -w 4 -b 0.0.0.0:8006 $FLASK_APP1 & gunicorn -w 4 -b 0.0.0.0:8007 $FLASK_APP2 & gunicorn -w 4 -b 0.0.0.0:8008 $FLASK_APP3 & wait"]

# ENTRYPOINT ["gunicorn", "-w", "4", "-b", "0.0.0.0:8006", "--access-logfile", "access.log", "--error-logfile", "error.log"]
# CMD ["app:app"]