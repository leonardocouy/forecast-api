from ..db import db

class Address(db.Model):
    __tablename__ = "addresses"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cep = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return f"<Address { self.name }>"
