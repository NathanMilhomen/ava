from main.models.Subject import SubjectModel
from flask_restful import Resource, reqparse

# TODO: Fazer com que apenas ADMs consigam modificar 'subjects'


class SubjectRegister(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('name', type=str, required=True,
                        help='Subject name required')
    parser.add_argument('workload', type=float, required=True,
                        help='Subject workload required')
    parser.add_argument('number_of_classes', type=int, required=True,
                        help='Number of classes required')
    parser.add_argument('requirement_id', type=int, required=False,
                        help='Id of the required subject')

    def post(self):
        args = self.parser.parse_args()

        try:
            subject = SubjectModel.query.filter_by(name=args['name']).first()

            if not subject:
                subject = SubjectModel(**args)
                subject.save()

                return {'message': 'Subject created successfully'}, 201

            return {'message': f'Subject {args["name"]} already exists'}

        except Exception as e:
            print(e)
            return {'message': 'Something got wrong'}, 500


class Subjects(Resource):

    def get(self):

        subjects = SubjectModel.query.all()

        if subjects:
            subjects = [subject.jsonify() for subject in subjects]
            return subjects, 200

        return {'message': 'There is not subjects registered'}, 404


class Subject(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('name', type=str, required=True,
                        help='Subject name required')
    parser.add_argument('workload', type=float, required=True,
                        help='Subject workload required')
    parser.add_argument('number_of_classes', type=int, required=True,
                        help='Number of classes required')
    parser.add_argument('requirement_id', type=int, required=False,
                        help='Id of the required subject')

    def put(self, id):
        args = self.parser.parse_args()
        try:
            subject = SubjectModel.query.get(id)

            if subject:
                subject.update(args)
                return {'message': 'subject modified successfully'}, 200

            return {'message': 'Subject not found'}, 404

        except Exception as e:
            print(e)
            return {'message': 'Something got wrong'}, 500

    def get(self, id):
        subject = SubjectModel.query.get(id)
        if subject:
            return subject.jsonify(), 200

        return {'message': 'Subject not found'}, 404

    def delete(self, id):
        subject = SubjectModel.query.get(id)
        if subject:
            subject.delete()
            return {'message': 'Subject deleted'}, 200

        return {'message': 'Subject not found'}, 404
