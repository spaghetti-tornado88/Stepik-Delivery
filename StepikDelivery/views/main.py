from flask import render_template, session
import random

from StepikDelivery import app
from StepikDelivery.models.category import Category

@app.route('/')
def main_page():
    meals_to_show = []
    for row in Category.query.join(Category.meals):
        meals_to_show.append([row, *random.sample(row.meals, 3 if len(row.meals) > 3 else len(row.meal))])
    return render_template('main.html', meals=random.sample(meals_to_show, 4),
                           cart=session.get('cart', []), is_logged=session.get('user', []))