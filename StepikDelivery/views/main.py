from flask import render_template
from sqlalchemy import func
import random
import json

from StepikDelivery import app
from StepikDelivery.models.category import Category
from StepikDelivery import db
from StepikDelivery.models.user import User
from StepikDelivery.models.meal import Meal
from StepikDelivery.models.order import Order

@app.route('/')
def main_page():
    meals_to_show = []
    for row in Category.query.join(Category.meals):
        print(row)
        meals_to_show.append([row, *random.sample(row.meals, 3 if len(row.meals) > 3 else len(row.meal))])
    return render_template('main.html', meals=random.sample(meals_to_show, 4))