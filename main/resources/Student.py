from flask_restful import Resource, reqparse, request
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, get_raw_jwt
)

from main.models.Student import StudentModel
# from blacklist import BLACKLIST

parser = reqparse.RequestParser()
parser.add_argument('id', type=str, required=True,
                    help='Student identifier required')
parser.add_argument('first_name', type=str, required=True,
                    help='Student first name required')
parser.add_argument('last_name', type=str, required=True,
                    help='Student last name required')
parser.add_argument('password', type=str, required=True,
                    help='Student password required')
parser.add_argument('email', type=str, required=True,
                    help='Student email required')
parser.add_argument('course_id', type=int, required=True,
                    help='Course identifier required')
parser.add_argument('classroom_id', type=int, required=True,
                    help='Classroom identifier required')
parser.add_argument('university_id', type=int,
                    required=True, help='University identifier required')


class Student(Resource):

    def get(self, id):
        student = StudentModel.query.get(id)
        if student:
            json = student.jsonify()

            return json, 200

        return {'message': 'Student not found'}, 404


class StudentRegister(Resource):
    def post(self):
        try:
            args = parser.parse_args()
            student = StudentModel.query.get(args['id'])

            if not student:
                student = StudentModel.query.filter_by(
                    email=args['email']).first()

                if not student:
                    student = StudentModel(**args)
                    student.save()

                    return {'message': 'Student saved sucessfully'}, 201

                return {'message': 'Student email already registered'}, 400

            return {'message': "Student id already registered"}, 400

        except:
            return {'message': 'Something got wrong'}, 500