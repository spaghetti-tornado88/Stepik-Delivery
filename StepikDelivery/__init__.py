from flask import Flask

from StepikDelivery.extensions import migrate, db, admin
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

from StepikDelivery import models

db.init_app(app)
migrate.init_app(app, db)

import StepikDelivery.views