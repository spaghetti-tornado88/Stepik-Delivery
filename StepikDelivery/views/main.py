from flask import render_template
from sqlalchemy import func
import random


from StepikDelivery import app
from StepikDelivery.models.category import Category

@app.route('/')
def main_page():
    meals_to_show = []
    for row in Category.query.join(Category.meals):
        meals_to_show.append(random.sample(row.meals, 3 if len(row.meals) > 3 else len(row.meal)))
    return render_template('main.html', meals=random.sample(meals_to_show, 4))