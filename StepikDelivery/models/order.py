from datetime import datetime

from StepikDelivery import db
from StepikDelivery.models.relations import meals_in_order
from StepikDelivery.models.mixin import BaseMixin


class Order(db.Model, BaseMixin):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(), default=datetime.utcnow())
    summary = db.Column(db.Float(10, 2))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='orders')
    meals = db.relationship('Meal', secondary=meals_in_order, back_populates='orders')