from flask import render_template, session

from StepikDelivery import app


@app.route('/account')
def account_page():
    return render_template('account.html', cart=session.get('cart', []), is_logged=session.get('user', []))