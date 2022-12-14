from flask import Flask , jsonify
from app import run_app
from flask_sqlalchemy import SQLAlchemy
import json

app = run_app()



@app.route('/')
def index():
    u = []
    with app.app_context():
        from app.models.models import User
        users = User.getAll()
        jsn = [{"id": u.id, "username": u.username} for u in users]
    return jsn or []


if __name__ == '__main__':
    app.run(debug=True,  host="0.0.0.0", port=5000)
 