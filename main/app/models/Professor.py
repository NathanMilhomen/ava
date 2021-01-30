from main.app import db, bcrypt

from main.app.models import Subject, Quiz

professor_subject = db.Table(
    'professor_subject',
    db.Column('professor_id', db.String(11), db.ForeignKey(
        'professor.id'), primary_key=True),
    db.Column('subject_id', db.Integer, db.ForeignKey(
        'subject.id'), primary_key=True)
)


class ProfessorModel(db.Model):

    __tablename__ = 'professor'

    id = db.Column(db.String(11), primary_key=True)

    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(60), nullable=False)

    # Relationships
    quizes = db.relationship('QuizModel', backref='professor',
                             lazy='select', cascade='all, delete-orphan')
    subjects = db.relationship(
        'SubjectModel', secondary=professor_subject,
        backref=db.backref('professor', lazy='dynamic'))

    def __init__(self, id: str, first_name: str, last_name: str, email: str, password: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf8')
