import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import stripe

db = SQLAlchemy()
login = LoginManager()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///app.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    stripe_keys = {
        "secret_key": "sk_test_51KuoTKFKJtp0R2ukHEMD8PH6zWqhqb5XypBjpNEVaWEF56VplXlcRhYvToJIYi0Eko7V5WrwX5eaBaBEYtbZC15E00BGHsHKAm",
        "publishable_key": "pk_test_51KuoTKFKJtp0R2ukxATfmz9S27qY6erPNcEypmUi0OteozFaEx3tznS0dBjXE3jdoF0EZ1W00FTsrbQlsByYmpNI00aISeT6A8",
    }

    stripe.api_key = stripe_keys["secret_key"]

    db.init_app(app)
    login.init_app(app)
    login.login_view = 'login'

    from . import routes, models
    app.register_blueprint(routes.bp)
    app.register_blueprint(models.bp)

    with app.app_context():
        db.create_all()

    return app
