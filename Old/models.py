
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


db = SQLAlchemy()

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



class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(), default=datetime.utcnow())
    summary = db.Column(db.Float(10, 2))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='orders')
    meals = db.relationship('Meal', secondary=meals_in_order, lazy='subquery', back_populates='orders')


class Meal(db.Model):
    __tablename__ = 'meals'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    price = db.Column(db.Float(5, 2), nullable=False)
    description = db.Column(db.String(), nullable=False)
    picture = db.Column(db.String(), nullable=False)
    orders = db.relationship('Order', secondary=meals_in_order, lazy='subquery', back_populates='meals')
    categories = db.relationship('Category', secondary=meals_in_category, lazy='subquery', back_populates='meals')


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    meals = db.relationship('Meal', secondary=meals_in_category, lazy='subquery', back_populates='categories')


# for cat in ['sushi', 'pizza' ,'pasta' , 'streetfood', 'new' ,'salads']:
#     category = Category(title=cat)
#     db.session.add(category)
#
# db.session.commit()
#
# with open('data.json', 'r') as file:
#     json_file = json.loads(file.read())
#
#
#
# for item in json_file:
#     #print(item, item['title'])
#     meal = Meal(title=item['title'],
#                 price=item['price'],
#                 description=item['description'],
#                 picture=item['picture'])
#     db.session.add(meal)
#     for cat in item['category'].split():
#         category = db.session.query(Category).filter(Category.title==cat).first()
#         meal.categories.append(category)
#
# db.session.commit()
#
# # for meal in db.session.query(Meal).all():
# #     print(meal.title, meal.categories)
#
# with open('users.json', 'r') as file:
#     json_file = json.loads(file.read())
#
# for user in json_file:
#     print(user)
#     user = User(name = user['name'], email=user['email'], password=user['password'], adress=user['adress'])
#     db.session.add(user)
#
# db.session.commit()
#
# order = Order()
# usr = db.session.query(User).filter(User.id == 2).one()
# order.user = usr
# ml = db.session.query(Meal).get(1)
# order.summary = ml.price
# order.meals.append(ml)
# db.session.add(order)
# db.session.commit()