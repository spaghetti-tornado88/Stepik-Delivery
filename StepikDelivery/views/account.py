from flask import render_template

from StepikDelivery import app


@app.route('/account')
def account_page():
    return render_template('account.html')