from StepikDelivery import app

from flask_admin.contrib.sqla import ModelView

from StepikDelivery.models.user import User
from StepikDelivery.models.order import Order
from StepikDelivery.models.meal import Meal
from StepikDelivery.models.category import Category
from StepikDelivery import admin, db

admin.init_app(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Order, db.session))
admin.add_view(ModelView(Meal, db.session))
admin.add_view(ModelView(Category, db.session))

if __name__ == "__main__":
    app.run()
