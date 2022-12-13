from flask import Flask
from .config import AppConfig



def run_app(config=AppConfig):
    

    app = Flask(__name__)

    app.config.from_object(AppConfig)


    return app


