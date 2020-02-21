from StepikDelivery import db
from StepikDelivery.models.relations import meals_in_category
from StepikDelivery.models.mixin import BaseMixin


class Category(db.Model, BaseMixin):
    __tablename__ = 'categories'

    title = db.Column(db.String(100), unique=True, nullable=False)
    meals = db.relationship('Meal', secondary=meals_in_category, back_populates='categories')
