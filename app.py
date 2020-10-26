import os
from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
from flask.logging import default_handler

app = Flask(__name__, template_folder='project/templates')

#Configuration
config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
app.config.from_object(config_type)

#Removing the default Logger config'd by Flask
app.logger.removeHandler(default_handler)

#Logging config
file_handler = RotatingFileHandler('instance/flask-stock-port.log', maxBytes=16384, backupCount=20)
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s in [in %(filename)s:%(lineno)d]')
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

#Log Flask app start
app.logger.info('Starting Flask Stock Portfolio App...')

from project.stocks import stocks_blueprint
from project.users import users_blueprint

app.register_blueprint(stocks_blueprint)
app.register_blueprint(users_blueprint, url_prefix='/users')




