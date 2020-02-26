from flask import render_template, session, redirect, url_for, flash, request

from StepikDelivery import app, db
from StepikDelivery.models.meal import Meal
from StepikDelivery.models.order import Order
from StepikDelivery.models.user import User
from StepikDelivery.forms.register import RegisterForm


@app.route('/cart', methods=['POST', 'GET'])
def cart_page():
    cart_items = []
    summary = 0

    for meal_id in session.get('cart', []):
        meal = Meal.query.get(meal_id)
        cart_items.append(meal)
        summary += meal.price

    if session.get('user'):
        make_order = RegisterForm()
        if make_order.is_submitted() and session['cart']:
            logged_user = User.query.get(session['user'][0])
            new_order = Order(summary=summary, user=logged_user, status=1)
            for meal_id in session['cart']:
                new_order.meals.append(Meal.query.get(meal_id))
            db.session.add(new_order)
            db.session.commit()
            session['cart'] = []
            return redirect(url_for('order_accepted_page'))

    register = RegisterForm()
    user_in_db = User.query.filter(User.email == register.email.data).all()

    if request.method == 'POST' and not user_in_db and session.get('cart', []) and register.validate_on_submit():
        new_user = User(name=register.name.data, adress=register.adress.data,
                        email=register.email.data, password=register.password.data, role=1)
        db.session.add(new_user)
        db.session.commit()
        new_order = Order(summary=summary, user=new_user, status=1)
        db.session.add(new_order)

        for meal_id in session['cart']:
            new_order.meals.append(Meal.query.get(meal_id))
        db.session.commit()
        session['cart'] = []
        return redirect(url_for('order_accepted_page'))

    if not session.get('cart'):
        flash('Корзина пуста')
    if user_in_db:
        flash('Пользователь с данной почтой уже зарегистрирован')
    return render_template('cart.html', cart=session.get('cart', []), is_logged=session.get('user', []),
                           cart_items=cart_items, summary=summary, form=register)


@app.route('/add_to_cart/<int:product_id>')
def add_to_cart_page(product_id):
    cart = session.get('cart', [])
    if product_id not in cart:
        cart.append(product_id)
    session['cart'] = cart
    flash('Блюдо добавленно в корзину')
    return redirect(url_for('cart_page'))


@app.route('/del_from_cart/<int:product_id>')
def del_from_cart_page(product_id):
    cart = session.get('cart')
    cart.remove(product_id)
    session['cart'] = cart
    flash('Блюдо удалено из корзины')
    return redirect(url_for('cart_page'))


@app.route('/order_accepted')
def order_accepted_page():
    return render_template('order_accepted.html', cart=session.get('cart', []), is_logged=session.get('user', []))