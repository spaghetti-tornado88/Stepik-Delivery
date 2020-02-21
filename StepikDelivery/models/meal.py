from StepikDelivery import db
from StepikDelivery.models.mixin import BaseMixin
from StepikDelivery.models.relations import meals_in_order, meals_in_category


class Meal(db.Model, BaseMixin):
    __tablename__ = 'meals'

    title = db.Column(db.String(100), unique=True)
    price = db.Column(db.Float(5, 2), nullable=False)
    description = db.Column(db.String(), nullable=False)
    picture = db.Column(db.String(), nullable=False)
    orders = db.relationship('Order', secondary=meals_in_order, back_populates='meals')
    categories = db.relationship('Category', secondary=meals_in_category, back_populates='meals')
