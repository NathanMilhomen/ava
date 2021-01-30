from main.app import create_app
from main.app.models.Student import StudentModel
from main.app.models.Course import CourseModel
from main.app.models.Classroom import ClassroomModel
from main.app.models.University import UniversityModel

from main.app.utils.models import save_model, delete_model


app = create_app()
app.app_context().push()

course_id = CourseModel.query.filter_by(name='Engineering').first().id
classroom_id = ClassroomModel.query.get(1).id
university_id = UniversityModel.query.filter_by(
    name='UniEvangelica').first().id

student = StudentModel(
    '2011687', 'Foo', 'Bar', 'password',
    'email@outlook.com', course_id, classroom_id, university_id)

save_model(student)
