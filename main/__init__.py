from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt
from decouple import config

from main.utils.models import AvaModel


db = SQLAlchemy(model_class=AvaModel)
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.config['JSON_SORT_KEYS'] = False
    app.config['JWT_SECRET_KEY'] = 'SECRET'
    db.init_app(app)
    bcrypt.init_app(app)
    jwt = JWTManager(app)

    return app
