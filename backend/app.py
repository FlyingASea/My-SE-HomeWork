import json
import os
from datetime import timedelta

from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import generate_csrf, CSRFProtect, CSRFError
from sqlalchemy import desc
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SECRET_KEY"] = os.urandom(32)
db = SQLAlchemy(app)
csrf = CSRFProtect()


def get_password(password):
    return generate_password_hash(password)


class User(db.Model):
    id = db.Column("id", db.String(80), primary_key=True, unique=True, nullable=False)
    name = db.Column("name", db.String(255), nullable=False)
    password_hash = db.Column("password", db.String(255), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@app.route("/query/id", methods=["GET"])
def query_id():
    if request.method == "GET":
        data = json.loads(request.get_data())
        result = User.query.filter_by(id=data["id"]).first()
        if result is None:
            return json.dumps({'errorCode': '500', 'content': 'query failed'})
        else:
            print(result)
            return json.dumps({'id': result.title, 'name': result.name})
    else:
        return json.dumps({'errorCode': '425', 'content': 'method d'})


@csrf.exempt
@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        data = json.loads(request.get_data())
        id = data['id']
        password = data['password']
        result = User.query.filter_by(id=data["id"]).first()
        if result is None:
            return json.dumps({'errorCode': '409', 'content': 'not have this user'})
        else:
            if result.check_password(password):
                # if check_password_hash(result.password_hash, password):
                print("Login ok")
                return json.dumps({'id': data['id']})
            else:
                print(str(id))
                return "POST Method"
    else:
        return "GET Method"


@csrf.exempt
@app.route("/add", methods=["POST"])
def add():
    if request.method == "POST":
        print(request.headers)
        data = json.loads(request.get_data())
        user1 = User(id=data['id'], name=data['name'])
        user1.set_password(str(data['password']))
        db.session.add(user1)
        db.session.commit()
    return 'ok'


@app.route("/change/name", methods=["POST"])
def change_name():
    if request.method == "POST":
        data = json.loads(request.get_data())
        User.query.filter(User.id == data['id']).update({'name': data['name']})
        db.session.commit()
    return 'ok'


@app.route("/change/password", methods=["POST"])
def change_password():
    if request.method == "POST":
        data = json.loads(request.get_data())
        User.query.filter(User.id == data['id']).update({'password': get_password(data['password'])})
        db.session.commit()
    return 'ok'


@app.route("/delete", methods=["GET"])
def delete():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)
    session['user'] = '123'
    return 'ok'


@app.route("/verify", methods=["GET"])
def verify():
    if 'user' in session:
        if session['user'] == '123':
            return 'ok'
        else:
            print("user not the 123")
    else:
        print("not have the user")
    return 'false'


@app.route("/logout", methods=["POST"])
def logout():
    session.pop('username', None)
    return 'ok'


@app.route("/getC", methods=["GET"])
def getC():
    print(request.headers)
    result = User.query.with_entities(User.id, User.name).order_by(desc(User.id)).all()
    res = []
    for row in result:
        print(row)
        step = {'id': row[0], 'name': row[1]}
        res.append(step)
    return json.dumps(res)


@app.after_request
def after_request(response):
    if response:
        csrf_token = generate_csrf()
        response.set_cookie('X-CSRFToken', csrf_token)
    return response


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    print(request.headers)
    print(e.description)
    return e.description


with app.app_context():
    csrf.init_app(app)
    db.create_all()
    app.run(debug=True)
