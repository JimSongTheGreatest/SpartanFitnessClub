import flask 
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

application = flask.Flask(__name__)

application.config.from_mapping(
        SECRET_KEY = 'it-dont-matter',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False

)

db = SQLAlchemy(application)
login = LoginManager(application)
login.login_view = 'login'

from myapp import routes, models
