import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.config import ENV_CONFIG


FLASK_ENV = os.environ.get('FLASK_ENV', 'production')

app = Flask(__name__)
db = SQLAlchemy(app)


from src import routes
from src.articles.routes import article_pages


app.register_blueprint(article_pages, url_prefix='/articles')
app.config.from_object(ENV_CONFIG[FLASK_ENV])

