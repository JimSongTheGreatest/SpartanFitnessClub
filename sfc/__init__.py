import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login = LoginManager()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///app.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    db.init_app(app)
    login.init_app(app)
    login.login_view = 'login'

    from . import routes, models
    app.register_blueprint(routes.bp)
    app.register_blueprint(models.bp)

    with app.app_context():
        db.create_all()

    return app
