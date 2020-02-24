from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, Length, EqualTo, ValidationError
import phonenumbers




class RegisterForm(FlaskForm):
    name = StringField('Ваше имя', description='Введите ваше имя',
                       validators=[DataRequired('Это поле не может быть пустым')])
    adress = StringField('Адрес', description='Введите адрес доставки',
                          validators=[DataRequired('Это поле не может быть пустым')])
    email = StringField('Почта', description='Введите вашу почту',
                        validators=[DataRequired('Это поле не может быть пустым'),
                                    Email('Введеный e-mail имеет неправильный формат')])
    phone = StringField('Телефон', description='Введите ваш телефон',
                        validators=[DataRequired('Это поле не может быть пустым')])
    password = PasswordField('Пароль', description='Введите пароль',
                           validators=[DataRequired('Это поле не может быть пустым'),
                                       Length(8, message='Слишком короткий пароль'),
                                       EqualTo('password_confirm', 'Пароли должны совпадать')])
    password_confirm = PasswordField('Повторите пароль')
    submit = SubmitField('Зарегистрироваться\n и оформить заказ')

    def validate_phone(self, field):
        if not phonenumbers.is_valid_number(phonenumbers.parse(field.data, 'RU')):
            raise ValidationError('Введенный телефон имеет недопустимый формат')