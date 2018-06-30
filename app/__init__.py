from flask import Flask
from flask_assets import Bundle, Environment

app = Flask(__name__)

js = Bundle('home.js', 'add.js', 'subtract.js', output='gen/main.js', filters='jsmin')

assets = Environment(app)

assets.register('main_js', js)

from app import routes
