from flask import render_template

from StepikDelivery import app
# from StepikDelivery import db
# from StepikDelivery.models.user import User

@app.route('/')
def main_page():
    return render_template('main.html')