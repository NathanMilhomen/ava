from datetime import datetime

from main.app import db
from main.app.models import Question, Professor

quiz_question = db.Table(
    'quiz_question',
    db.Column('quiz_id', db.Integer, db.ForeignKey(
        'quiz.id'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey(
        'question.id'), primary_key=True)
)


class QuizModel(db.Model):

    __tablename__ = 'quiz'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_date = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    final_date = db.Column(db.DateTime, nullable=False)
    num_of_questions = db.Column(db.Integer, nullable=False, default=1)
    grade = db.Column(db.Float, nullable=False, default=0)

    # Relationships
    subject_id = db.Column(db.Integer, db.ForeignKey(
        'subject.id'), nullable=False)

    professor_id = db.Column(db.String(11), db.ForeignKey(
        'professor.id'), nullable=False)

    questions = db.relationship('QuestionModel', secondary=quiz_question,
                                lazy='select', backref=db.backref('quiz', lazy='select'))

    def __init__(self, start_date: datetime, final_date: datetime, num_of_questions: int, grade: float, subject_id: int, professor_id: str):
        self.start_date = start_date
        self.final_date = final_date
        self.num_of_questions = num_of_questions
        self.grade = grade
        self.subject_id = subject_id
        self.professor_id = professor_id
