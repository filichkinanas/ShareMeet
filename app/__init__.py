from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_qrcode import QRcode
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
QRcode(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models