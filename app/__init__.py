from flask import Flask
from .config import AppConfig



def run_app(config=AppConfig):
    

    app = Flask(__name__)

    app.config.from_object(AppConfig)
    
    from app.models import db
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    return app


