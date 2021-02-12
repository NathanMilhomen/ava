from flask_restful import Api

from main.resources.Student import StudentRegister, StudentLogin, StudentLogout, Students, Student


def add_resources(app):
    api = Api(app)

    api.add_resource(StudentRegister, '/student')
    api.add_resource(StudentLogin, '/student/login')
    api.add_resource(StudentLogout, '/student/logout')
    api.add_resource(Students, '/students')
    api.add_resource(Student, '/student/<string:id>')
