from flask_restful import Api

from main.resources.Student import StudentRegister, StudentLogin, StudentLogout, Students, Student
from main.resources.Subject import SubjectRegister, Subjects, Subject


def add_resources(app):
    api = Api(app)

    # Students
    api.add_resource(StudentRegister, '/student')
    api.add_resource(StudentLogin, '/student/login')
    api.add_resource(StudentLogout, '/student/logout')
    api.add_resource(Students, '/students')
    api.add_resource(Student, '/student/<string:id>')

    # Subjects
    api.add_resource(SubjectRegister, '/subject')
    api.add_resource(Subjects, '/subjects')
    api.add_resource(Subject, '/subject/<string:id>')
