from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


from main import create_app, db
from main.utils.resources import add_resources
from main.models import (
    Classroom, Course, Professor, Question,
    QuestionOption, Quiz, SchoolRecord, Student, Subject, University
)


app = create_app()
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    add_resources(app)
    app.run(debug=True)


if __name__ == '__main__':
    manager.run()
