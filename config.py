import os 

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('FSP_SECRET_KEY', default='THIS_IS_NOT_SECUREhsehf98hw9dsh')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', default=f"sqlite:///{os.path.join(BASEDIR, 'instance', 'app.db')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    FLASK_ENV = 'production'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True