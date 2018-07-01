from flask import Flask
from flask_assets import Bundle, Environment
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)

js = Bundle('home.js', 'add.js', 'subtract.js', output='gen/main.js', filters='jsmin')
assets = Environment(app)
assets.register('main_js', js)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

from app import routes, models  # noqa
