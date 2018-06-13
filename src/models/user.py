from ..db import db
from flask_bcrypt import Bcrypt


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    cities = db.relationship("City", backref="user", lazy="dynamic")

    def __init__(self, first_name, last_name, email, password, cities = []):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = Bcrypt().generate_password_hash(password).decode()
        self.cities = cities

    def __repr__(self):
        return f"<User { self.email }>"
