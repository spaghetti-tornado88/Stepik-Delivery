from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


MAX_VISITS = 5

app = Flask(__name__)
for env_var_name, env_var_val in os.environ.items():
    print(env_var_name, env_var_val)

app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

print(app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Visit(db.Model):
    __tablename__ = 'visits'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())


@app.route('/')
def home():
    visit = Visit()
    db.session.add(visit)
    db.session.commit()
    visits = Visit.query.order_by(Visit.created_at.desc()).all()
    return render_template("home.html", visits=visits)


