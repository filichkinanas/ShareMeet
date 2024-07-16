from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import qrcode
import qrcode.image.svg
import socket
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
_ip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close())
       for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
_link = f'http://{_ip}:5000/shared_files'
_qr_link = qrcode.make(_link, image_factory=qrcode.image.svg.SvgPathImage)
qr_svg = _qr_link.to_string(encoding='unicode')

from app import routes, models