from main import db


class SchoolRecordModel(db.Model):

    __tablename__ = 'school_record'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Divida em 3 avaliações
    first_grade = db.Column(db.Float, nullable=False, default=0)
    second_grade = db.Column(db.Float, nullable=False, default=0)
    third_grade = db.Column(db.Float, nullable=False, default=0)

    mean = db.Column(db.Float, nullable=False, default=0)
    missed_classes = db.Column(db.Integer, nullable=False, default=0)
    attendance = db.Column(db.Float, nullable=False, default=100)  # Frequencia

    # Relationships
    student_id = db.Column(db.String(8), db.ForeignKey(
        'student.id'))

    subject_id = db.Column(db.Integer, db.ForeignKey(
        'subject.id'), nullable=False)
