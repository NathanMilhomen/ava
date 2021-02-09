from main import db, bcrypt

from main.models import SchoolRecord, Quiz, Subject, Course, University, Classroom


student_subject = db.Table(
    'student_subject',
    db.Column('student_id', db.String(8), db.ForeignKey(
        'student.id'), primary_key=True),

    db.Column('subject_id', db.Integer, db.ForeignKey(
        'subject.id'), primary_key=True)
)

student_quiz = db.Table(
    'student_quiz',
    db.Column('student_id', db.String(8), db.ForeignKey(
        'student.id'), primary_key=True),
    db.Column('quiz_id', db.Integer, db.ForeignKey(
        'quiz.id'), primary_key=True),
)


class StudentModel(db.Model):

    __tablename__ = 'student'

    id = db.Column(db.String(8), primary_key=True)  # Número da matrícula
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)

    # Relationships
    course_id = db.Column(db.Integer, db.ForeignKey(
        'course.id'), nullable=False)
    classroom_id = db.Column(db.Integer, db.ForeignKey(
        'classroom.id'), nullable=False)
    university_id = db.Column(db.Integer, db.ForeignKey(
        'university.id'), nullable=False)

    school_records = db.relationship(
        'SchoolRecordModel', backref='student', lazy='select')

    quizes = db.relationship(
        'QuizModel', secondary=student_quiz, backref=db.backref('student', lazy='dynamic'))
    subjects = db.relationship(
        'SubjectModel', secondary=student_subject, backref=db.backref('student', lazy='dynamic'))

    def __init__(self, id: str, first_name: str, last_name: str, password: str, email: str, course_id: int, classroom_id: int, university_id: int, teste: str = 'Teste'):

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.course_id = course_id
        self.classroom_id = classroom_id
        self.university_id = university_id
