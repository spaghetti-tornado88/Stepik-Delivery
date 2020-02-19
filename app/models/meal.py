from app import db
from app.models.mixin import BaseMixin

class Meal(db.Model, BaseMixin):
    __tablename__ = 'meals'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    price = db.Column(db.Float(5, 2), nullable=False)
    description = db.Column(db.String(), nullable=False)
    picture = db.Column(db.String(), nullable=False)
    orders = db.relationship('Order', secondary=meals_in_order,
                             lazy='subquery', back_populates='meals')
    categories = db.relationship('Category', secondary=meals_in_category,
                                 lazy='subquery', back_populates='meals')