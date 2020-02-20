from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class LoginForm(FlaskForm):
    pass


class RegistrationForm(FlaskForm):
    pass


