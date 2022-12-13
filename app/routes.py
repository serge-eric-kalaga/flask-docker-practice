from flask import Flask, jsonify
from . import run_app

app = run_app()


@app.route('/')
def index():
    u = []
    with app.app_context():
        from .models import User
        u = User.getAll()
    return jsonify(u) or []