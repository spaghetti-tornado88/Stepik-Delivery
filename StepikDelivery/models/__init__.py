from StepikDelivery.models.relations import meals_in_category, meals_in_order
from StepikDelivery.models.user import User
from StepikDelivery.models.category import Category
from StepikDelivery.models.meal import Meal
from StepikDelivery.models.order import Order
from StepikDelivery import db

#db.create_all()

 __all__ = ["User", "Category", "Meal", "Order"]