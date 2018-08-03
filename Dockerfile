FROM python:3.7

EXPOSE 8080 8081

WORKDIR /app
COPY . /app

RUN useradd uwsgi

RUN pip3 install -r requirements.txt

USER uwsgi
CMD ["uwsgi", "--ini", "uwsgi.ini"]
