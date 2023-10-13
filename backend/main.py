import json
import os
from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import generate_csrf, CSRFProtect, CSRFError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SECRET_KEY"] = os.urandom(32)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)
db = SQLAlchemy(app)

csrf = CSRFProtect()


@app.after_request
def after_request(response):
    if response:
        csrf_token = generate_csrf()
        response.set_cookie('X-CSRFToken', csrf_token)
    return response


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return json.dumps({'errorCode': 104, 'httpCode': 403, 'desc': str(e.description)})


with app.app_context():
    db.create_all()
    csrf.init_app(app)
    app.run(host="127.0.0.1", port=11451, debug=True)
