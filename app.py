from flask import Flask 
from app import run_app
from flask_sqlalchemy import SQLAlchemy

app = run_app()

from app.routes import *



if __name__ == '__main__':
    app.run(debug=True,  host="0.0.0.0", port=5000)
 