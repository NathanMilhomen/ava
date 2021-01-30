from main.app.utils.test_model import get_application
from main.app.models import Classroom, Course
from main.app.utils.models import save_model

get_application()

course_id = Course.CourseModel.query.filter_by(name="Engineering").first().id
first_class = Classroom.ClassroomModel(1, course_id)

save_model(first_class)
