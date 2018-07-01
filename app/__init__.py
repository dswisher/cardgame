from flask import Flask
from flask_assets import Bundle, Environment
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

js = Bundle('home.js', 'add.js', 'subtract.js', output='gen/main.js', filters='jsmin')

assets = Environment(app)

assets.register('main_js', js)

from app import routes      # noqa
