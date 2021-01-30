from main.app.models.QuestionOption import QuestionOptionModel
from main.app.utils.test_model import get_application
from main.app.utils.models import save_model

get_application()
# TODO: Testar isso depois de fazer o relacionamento
subject = QuestionOptionModel('asdsadsadasdsadsadsada', 1, False)

save_model(subject)
