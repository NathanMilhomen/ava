from decouple import config

from flask_sqlalchemy import Model

from sqlalchemy.orm.session import object_session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy_session import flask_scoped_session


engine = create_engine(config('DATABASE_URI'))
session_factory = sessionmaker(bind=engine)
session = flask_scoped_session(session_factory)


class AvaModel(Model):

    def save(self):
        session.add(self)
        session.commit()

    def delete(self):
        session = object_session(self)
        session.delete(self)
        session.commit()

    def update(self, args):
        for key, value in args.items():
            if value:
                setattr(self, key, value)

        session = object_session(self)
        session.add(self)
        session.commit()

    def jsonify(self):
        json = vars(self)
        json.pop('_sa_instance_state')

        return json
