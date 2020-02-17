from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'you-shall-not-pass'

db = SQLAlchemy(app)

meals_in_order = db.Table('meals_in_order',
                          db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), primary_key=True),
                          db.Column('meal_id', db.Integer, db.ForeignKey('meals.id'), primary_key=True)
                          )

meals_in_category = db.Table('meals_in_category',
                             db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True),
                             db.Column('meal_id', db.Integer, db.ForeignKey('meals.id'), primary_key=True)
                             )


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(50))
    adress = db.Column(db.String)
    orders = db.relationship('Order', back_populates='user')


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime())
    summary = db.Column(db.Float(10, 2))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='orders')
    meals = db.relationship('Meal', secondary=meals_in_order, lazy='subquery', back_populates='orders')


class Meal(db.Model):
    __tablename__ = 'meals'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    price = db.Column(db.Float(5, 2))
    description = db.Column(db.String())
    picture = db.Column(db.String())
    orders = db.relationship('Order', secondary=meals_in_order, lazy='subquery', back_populates='meals')
    categories = db.relationship('Category', secondary=meals_in_category, lazy='subquery', back_populates='meals')


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    meals = db.relationship('Meal', secondary=meals_in_category, lazy='subquery', back_populates='categories')

db.create_all()

with open('data.json', 'r') as file:
    json_file = json.loads(file.read())

for item in json_file:
    print(item, item['title'])
    meal = Meal(title=item['title'],
                price=item['price'],
                description=item['description'],
                picture=item['picture'],)
    meal.categories = item['category']
    db.session.add(meal)
db.session.commit()
                #categories=item['category'])