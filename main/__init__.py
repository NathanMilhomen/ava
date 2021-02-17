from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

from main.utils.models import AvaModel
from main.config import DevelopmentConfig


db = SQLAlchemy(model_class=AvaModel)
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    return app
