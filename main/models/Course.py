from main import db

from main.models import Student, Classroom, Subject


course_subject = db.Table(
    'course_subject',
    db.Column('course_id', db.Integer, db.ForeignKey(
        'course.id'), primary_key=True),
    db.Column('subject_id', db.Integer, db.ForeignKey(
        'subject.id'), primary_key=True)
)


class CourseModel(db.Model):

    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

    # Relationships

    students = db.relationship(
        'StudentModel', backref='course', lazy='select', cascade='all, delete-orphan')
    classrooms = db.relationship(
        'ClassroomModel', backref='course', lazy='select', cascade='all, delete-orphan')

    subjects = db.relationship(
        'SubjectModel', secondary=course_subject,
        backref=db.backref('course', lazy='select'))

    def __init__(self, name: str):
        self.name = name
