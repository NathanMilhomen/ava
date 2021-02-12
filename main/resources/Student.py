from datetime import datetime, timezone

from flask_restful import Resource, reqparse, request
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, get_raw_jwt
)
from main import bcrypt
from main.models.Student import StudentModel
from main.models.BlacklistedToken import BlacklistedToken
# from blacklist import BLACKLIST

# TODO: Implementar STUDENT login, logout


class StudentRegister(Resource):

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

    def post(self):
        args = self.parser.parse_args()

        try:
            student = StudentModel.query.get(args['id'])

            if not student:
                student = StudentModel.query.filter_by(
                    email=args['email']).first()

                if not student:
                    args['password'] = bcrypt.generate_password_hash(
                        args['password']).decode('utf8')

                    student = StudentModel(**args)
                    student.save()

                    return {'message': 'Student saved sucessfully'}, 201

                return {'message': 'Student email already registered'}, 400

            return {'message': "Student id already registered"}, 400

        except Exception as e:
            print(e)
            return {'message': 'Something got wrong'}, 500


class StudentLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=str, required=True,
                        help='Student identifier requireed')
    parser.add_argument('password', type=str, required=True,
                        help='Student password required')

    def post(self):
        args = self.parser.parse_args()

        try:
            student = StudentModel.query.get(args['id'])

            if student:
                password = student.password
                correct = bcrypt.check_password_hash(
                    password, args['password'])

                if correct:
                    acess_token = create_access_token(identity=student.id)
                    return {
                        'message': 'Logged successfully',
                        'acess_token': acess_token
                    }

                return {'message': 'Invalid credencials'}

            return {'message': 'Invalid credencials'}

        except Exception as e:
            print(e)
            return {'message': 'Something got wrong'}


class Students(Resource):

    @jwt_required
    def get(self):
        students = StudentModel.query.all()
        students = [student.jsonify() for student in students]

        return students, 200


class Student(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('id', type=str)
    parser.add_argument('first_name', type=str)
    parser.add_argument('last_name', type=str)
    parser.add_argument('password', type=str)
    parser.add_argument('email', type=str)
    parser.add_argument('course_id', type=int)
    parser.add_argument('classroom_id', type=int)
    parser.add_argument('university_id', type=int)

    @jwt_required
    def get(self, id):
        student = StudentModel.query.get(id)
        if student:
            json = student.jsonify()

            return json, 200

        return {'message': 'Student not found'}, 404

    @jwt_required
    def put(self, id):

        args = Student.parser.parse_args()
        try:
            student = StudentModel.query.get(id)

            if student:
                args['password'] = bcrypt.generate_password_hash(
                    args['password']).decode('utf8') if args['password'] else None

                student.update(args)
                return {'message': 'Student modified successfully'}, 200

            return {'message': 'Student not found'}, 404

        except Exception as e:
            print(e)
            return {'message': 'Something got wrong'}, 500

    @jwt_required
    def delete(self, id):
        try:
            student = StudentModel.query.get(id)
            if student:
                student.delete()

                return {'message': 'Student deleted successfully'}, 200

            return {'message': 'Student not found'}, 404

        except Exception as e:
            print(e)
            return {'message': 'Something got wrong'}, 500


class StudentLogout(Resource):

    @jwt_required
    def get(self):
        jwt = get_raw_jwt()

        expires = datetime.fromtimestamp(jwt['exp'], tz=timezone.utc)
        token = BlacklistedToken(
            jti=jwt['jti'],
            identity=jwt['identity'],
            expires=expires
        )

        token.save()

        return {'message': 'Logged out successfully'}, 200
