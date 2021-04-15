import os
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from src.config import ENV_CONFIG


FLASK_ENV = os.environ.get('FLASK_ENV', 'production')

app = Flask(__name__)
app.config.from_object(ENV_CONFIG[FLASK_ENV])

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth_pages.login'

from src import routes

from src.articles.routes import article_pages
app.register_blueprint(article_pages, url_prefix='/articles')

from src.auth.routes import auth_pages
app.register_blueprint(auth_pages, url_prefix='/auth')
