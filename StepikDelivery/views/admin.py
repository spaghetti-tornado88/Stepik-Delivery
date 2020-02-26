from flask import url_for, redirect, request, session, flash

from StepikDelivery import app

@app.before_request
def admin_access_control():
    if 'admin' in request.url:
        user = session.get('user')
        if not user or user[3] < 100:
            flash('Войдите, чтобы получить доступ к этой странице')
            return redirect(url_for('login_page'))