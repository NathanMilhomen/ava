from datetime import timedelta
from decouple import config


class Config:
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URI')
    JSONIFY_PRETTYPRINT_REGULAR = True
    JSON_SORT_KEYS = False
    JWT_SECRET_KEY = '1ahg83lasdin47sssjjjfnihok'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', ]
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    # DATABASE_URI = 'mysql://user@localhost/foo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URI')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# app.config['JSON_SORT_KEYS'] = False
# app.config['JWT_SECRET_KEY'] = 'SECRET'
# app.config['JWT_BLACKLIST_ENABLED'] = True
# app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', ]
# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)
