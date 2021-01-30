from main.app.models.Student import StudentModel
from main.app.utils.test_model import get_application
from main.app.utils.models import save_model, delete_model
from main.app import bcrypt


get_application()


def get_password(password):
    student = StudentModel.query.filter_by(
        first_name='Foo').first()
    pw_hash = student.password
    return bcrypt.check_password_hash(pw_hash, password)


def get_model(id):
    student = StudentModel.query.get(id)
    return student


def test_password():
    assert get_password('hash_password') == False


def test_password2():
    assert get_password('password') != False


def test_delete():
    model = get_model(2011687)
    delete_model(model)
    assert get_model(2011687) == None
