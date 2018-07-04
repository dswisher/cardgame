
from flask import Flask
from flask_assets import Bundle, Environment
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)

if app.config['DEBUG']:
    js_filters = None
else:
    js_filters = 'jsmin'

js_bundle = Bundle(
        'js/nav.js',
        output='gen/main.js',
        filters=js_filters)

less_bundle = Bundle(
        'less/main.less',
        output='gen/main.css',
        filters='less',
        depends=['less/*.less'])

assets = Environment(app)
assets.register('main_js', js_bundle)
assets.register('main_css', less_bundle)

# Rebuild the assets immediately, rather than waiting for page load
assets['main_js'].urls()
assets['main_css'].urls()

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

from app import routes, models, errors  # noqa
