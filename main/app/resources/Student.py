from flask_restful import Resource, reqparse, request

from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, get_raw_jwt
)
import bcrypt

from main.app.models.Student import StudentModel
# from blacklist import BLACKLIST


class Student(Resource):

    def get(self, id):
        student = StudentModel.query.get(id)
        if student:
            return student.__dict__

        return {'message': 'Student not found'}, 404
