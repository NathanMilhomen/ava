from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from main.app.models import (
    Classroom, Course, Professor, Question,
    QuestionOption, Quiz, SchoolRecord, Student, Subject, University
)
from main.app import create_app, db

app = create_app()

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()
