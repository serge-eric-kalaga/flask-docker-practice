FROM python:3.7.2-stretch

RUN apt-get -y update 
RUN apt install python3-pip -y

WORKDIR /flask_docker_test

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python", "app.py" ]