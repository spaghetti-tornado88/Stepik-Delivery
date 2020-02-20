from flask import Flask

from StepikDelivery.extensions import db, migrate, admin
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

import StepikDelivery.views