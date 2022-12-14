from flask import Flask , jsonify
from src import run_app
from flask_sqlalchemy import SQLAlchemy
import json

app = run_app()



@app.route('/')
def index():
    u = []
    with app.app_context():
        from src.models.models import User
        users = User.getAll()
        jsn = [{"id": u.id, "username": u.username} for u in users]
    return jsn 


if __name__ == '__main__':
    app.run(debug=True,  host="0.0.0.0", port=5000)
    
    with app.app_context():
        from src.models import *
        db.create_all()
        
    try :        
        user1 = User(username="serge")
        user2 = User(username="eric")
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
    except : pass
 