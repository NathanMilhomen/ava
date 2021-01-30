from main.app import db

from main.app.models import QuestionOption


class QuestionModel(db.Model):

    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    score = db.Column(db.Float, nullable=False, default=0.0)
    proposition = db.Column(db.Text, nullable=False)

    # Relationships
    options = db.relationship(
        'QuestionOptionModel', backref='question', lazy='select', cascade='all, delete-orphan')

    def __init__(self, score: float, proposition: str):
        self.score = score
        self.proposition = proposition
