from werkzeug.security import generate_password_hash, check_password_hash

from backend.main import db


class User(db.Model):
    id = db.Column("id", db.String(80), primary_key=True, unique=True, nullable=False)
    name = db.Column("name", db.String(255), nullable=False)
    _password_hash_ = db.Column("password", db.String(255), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def setPassword(self, password):
        self._password_hash_ = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self._password_hash_, password)
