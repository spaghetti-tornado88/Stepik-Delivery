from flask import render_template, session, request, redirect, url_for

from StepikDelivery import app
from StepikDelivery.forms.login import LoginForm
from StepikDelivery.models.user import User
from StepikDelivery.models.order import Order


@app.route('/login', methods=['GET','POST'])
def login_page():
    login = LoginForm()
    if request.method=='POST' and login.validate_on_submit():
        user = User.query.filter(User.email==login.email.data).one()
        if user.check_password(login.password.data):
            session['user'] = [user.id, user.email]
            orders = Order.query.filter(Order.user == user).all()
            return render_template('account.html', cart=session.get('cart', []), is_logged=session.get('user', []), orders=orders)
        else:
            login.password.errors.append('Пользователь с таким паролем не найден')
    return render_template('login.html', cart=session.get('cart', []), is_logged=session.get('user', []), form=login)


@app.route('/logout')
def logout_page():
    session['user'] = []
    return redirect(url_for('main_page'))

