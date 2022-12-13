from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    
    __tablename__ = "user"
    
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    
    def __init__(self, username=None) :
        self.username = username
        
    
    @classmethod
    def getAll(cls):
        return cls.query.all()
