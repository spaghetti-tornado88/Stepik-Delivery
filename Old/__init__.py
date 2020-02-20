from flask import Flask

from StepikDelivery.config import Confg
from StepikDelivery.models import db


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

from StepikDelivery.views import *


if __name__ == '__main__':
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    app.run()

