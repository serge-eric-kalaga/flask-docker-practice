FROM python:3.9-slim

RUN apt-get -y update 
RUN apt install python3-pip -y

WORKDIR /flask_docker_test

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD gunicorn --bind 0.0.0.0:5000 app:app