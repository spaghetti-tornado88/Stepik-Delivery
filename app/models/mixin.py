from app import db

class BaseMixin:

    id = db.Column(db.Integer, primary_key = True)
