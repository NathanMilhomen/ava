from main import db


class QuestionOptionModel(db.Model):

    __tablename__ = 'question_option'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.Text, nullable=False)
    correct = db.Column(db.Boolean, nullable=False, default=False)

    # Relationships
    question_id = db.Column(db.Integer, db.ForeignKey(
        'question.id'), nullable=False)

    def __init__(self, description: str, question_id: int, correct: bool = False):
        self.description = description
        self.question_id = question_id
        self.correct = correct
