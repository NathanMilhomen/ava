from main.app import create_app, db
from main.app.resources import Student
from flask_restful import Api

app = create_app()
app.app_context().push()

db.create_all(app=app)
db.session.commit()

api = Api(app)
api.add_resource(Student.Student, '/student/<string:id>')

# TODO: Implementar migrations

if __name__ == '__main__':
    app.run(debug=True)
