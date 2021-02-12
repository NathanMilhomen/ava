from datetime import datetime

from main import jwt
from main.models.BlacklistedToken import BlacklistedToken


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(token):
    token = BlacklistedToken.query.filter_by(jti=token['jti']).first()

    return token

# Mudando a mensagem


@jwt.unauthorized_loader
def unauthorized(msg):
    return {'message': 'You must be logged in'}, 401


@jwt.revoked_token_loader
def revoked_token():
    return {'message': 'Token revoked, you must login again'}


@jwt.expired_token_loader
def expired_token(msg):
    now = datetime.utcnow()
    expired_tokens = BlacklistedToken.query.filter(
        BlacklistedToken.expires < now).all()

    for token in expired_tokens:
        token.delete()

    return {'message': 'Token expired, you must login again'}
