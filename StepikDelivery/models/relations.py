from StepikDelivery import db


meals_in_order = db.Table('meals_in_order',
                          db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), primary_key=True),
                          db.Column('meal_id', db.Integer, db.ForeignKey('meals.id'), primary_key=True)
                          )

meals_in_category = db.Table('meals_in_category',
                             db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True),
                             db.Column('meal_id', db.Integer, db.ForeignKey('meals.id'), primary_key=True)
                             )
