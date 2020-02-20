from flask import render_template

from StepikDelivery import app


@app.route('/cart')
def cart_page():
    return render_template('cart.html')