from flask import render_template, session

from StepikDelivery import app
from StepikDelivery.models.order import Order
from StepikDelivery.models.user import User


@app.route('/account')
def account_page():
    user = User.query.get(session.get('user')[0])
    orders = Order.query.filter(Order.user==user).all()
    return render_template('account.html', cart=session.get('cart', []), is_logged=session.get('user', []), orders=orders)