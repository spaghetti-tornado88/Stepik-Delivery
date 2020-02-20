from flask import render_template

from StepikDelivery import app


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/logout')
def logout_page():
    return render_template('logout.html')