from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired('Введите почту')])
    password = PasswordField('Пароль', validators=[DataRequired('Введите пароль')])