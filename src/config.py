import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ConfigProduction(Config):
    pass


class ConfigDevelopment(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_DIR}../db.sqlite'


ENV_CONFIG = {
    'production': ConfigProduction,
    'development': ConfigDevelopment
}
