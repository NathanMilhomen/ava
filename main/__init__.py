from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from decouple import config

from main.utils.models import AvaModel


db = SQLAlchemy(model_class=AvaModel)
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.config['JSON_SORT_KEYS'] = False
    app.config['JWT_SECRET_KEY'] = 'SECRET'
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', ]
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    return app
