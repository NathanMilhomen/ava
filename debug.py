from main import create_app, db
from main.utils.resources import add_resources
from main.utils import autorization
from main.models import (
    Classroom, Course, Professor, Question,
    QuestionOption, Quiz, SchoolRecord, Student, Subject, University
)


app = create_app()
app.app_context().push()


if __name__ == '__main__':
    add_resources(app)
    app.run(debug=True)
