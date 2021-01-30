from main.app.models import Professor
from main.app.utils.test_model import get_application
from main.app.utils.models import save_model

get_application()

professor = Professor.ProfessorModel(
    '77766655511', 'Foo', 'Bar',
    'nathanmilhomen07@hotmail.com', 'hash_password')

save_model(professor)
