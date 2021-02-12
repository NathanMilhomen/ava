from main import db


class BlacklistedToken(db.Model):

    __tablename__ = 'blacklisted_token'

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    identity = db.Column(db.String(50), nullable=False)
    expires = db.Column(db.DateTime, nullable=False)

    def __init__(self, jti: str, identity: str, expires):
        self.jti = jti
        self.identity = identity
        self.expires = expires
