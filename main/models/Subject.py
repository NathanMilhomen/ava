from main import db

from main.models import SchoolRecord, Quiz


class SubjectModel(db.Model):

    __tablename__ = 'subject'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    workload = db.Column(db.Float, nullable=False)
    number_of_classes = db.Column(db.Integer, nullable=False)

    # Relationships
    requirement = db.relationship('SubjectModel', lazy='select')
    requirement_id = db.Column(db.Integer, db.ForeignKey('subject.id'))

    school_record = db.relationship(
        'SchoolRecordModel', backref='subject', lazy='select', cascade='all, delete-orphan')

    quizes = db.relationship('QuizModel', backref='subject',
                             lazy='select', cascade='all, delete-orphan')

    def __init__(self, name: str, workload: float, number_of_classes: int, requirement_id: int = None):
        self.name = name
        self.workload = workload
        self.number_of_classes = number_of_classes
        self.requirement_id = requirement_id

    def __repr__(self):
        return f'<SubjectModel {self.name}>'
