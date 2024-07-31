FROM python:3.9
LABEL maintainer="LinCenYing lincenying@gmail.com"
RUN pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip3 install -e .
EXPOSE 8006
ENTRYPOINT ["gunicorn", "-w", "4", "-b", "0.0.0.0:8006", "--access-logfile", "access.log", "--error-logfile", "error.log"]
CMD ["app:app"]