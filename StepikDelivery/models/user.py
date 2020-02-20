from werkzeug.security import generate_password_hash, check_password_hash

from StepikDelivery import db
from StepikDelivery.models.mixin import BaseMixin


class User(db.Model, BaseMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    adress = db.Column(db.String, nullable=False)
    orders = db.relationship('Order', back_populates='user')

    @property
    def password(self):
        raise AttributeError('This field is secure')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)