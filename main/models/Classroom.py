from main import db

from main.models import Student


class ClassroomModel(db.Model):

    __tablename__ = 'classroom'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    period = db.Column(db.Integer, nullable=False)

    # Relationships
    course_id = db.Column(db.Integer, db.ForeignKey(
        'course.id'), nullable=False)
    students = db.relationship(
        'StudentModel', backref='classroom', lazy='select')

    def __init__(self, period: int, course_id: int) -> None:
        self.period = period
        self.course_id = course_id
