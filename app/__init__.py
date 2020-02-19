from flask import Flask

from app.extensions import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

import app.views