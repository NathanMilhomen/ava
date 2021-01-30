# from main.app.models import Professor
# from main.app.utils.test_model import get_application
# from main.app.utils.models import save_model, delete_model
# from main.app import bcrypt


# get_application()


# def get_password(password):
#     professor = Professor.ProfessorModel.query.filter_by(
#         first_name='Foo').first()
#     pw_hash = professor.password
#     return bcrypt.check_password_hash(pw_hash, password)


# def get_model(id):
#     professor = Professor.ProfessorModel.query.get(id)
#     return professor


# def test_password():
#     assert get_password('hash_password') == True


# def test_password2():
#     assert get_password('password') != True


# def test_delete():
#     model = get_model(77766655511)
#     delete_model(model)
#     assert get_model(77766655511) == None
