from main.app import db

from main.app.models import Course, Student


university_course = db.Table('university_course',
                             db.Column('university_id', db.Integer, db.ForeignKey(
                                 'university.id'), primary_key=True),

                             db.Column('course_id', db.Integer, db.ForeignKey(
                                 'course.id'), primary_key=True)
                             )


class UniversityModel(db.Model):

    __tablename__ = 'university'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    # Relationships
    students = db.relationship(
        'StudentModel', backref='university', lazy='select')
    courses = db.relationship('CourseModel', secondary=university_course, lazy='select',
                              backref=db.backref('course', lazy='dynamic'))

    def __init__(self, name: str):

        self.name = name
