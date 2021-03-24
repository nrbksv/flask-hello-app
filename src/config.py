import os


class Config:
    DEBUG = False
    SECRET_KEY = os.environ['SECRET_KEY']


class ConfigProduction(Config):
    pass


class ConfigDevelopment(Config):
    ENV = 'development'
    DEBUG = True


ENV_CONFIG = {
    'production': ConfigProduction,
    'development': ConfigDevelopment
}
