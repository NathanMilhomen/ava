from flask_restful import Api

from main.resources import Student


def add_resources(app):
    api = Api(app)

    api.add_resource(Student.Students, '/students')
    api.add_resource(Student.Student, '/student/<string:id>')
    api.add_resource(Student.StudentRegister, '/student')
