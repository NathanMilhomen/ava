from main.app.models.Question import QuestionModel
from main.app.utils.test_model import get_application
from main.app.utils.models import save_model

get_application()

question = QuestionModel(
    50.0, "TesteTesteTesteTesteTesteTesteTesteTesteTesteTesteTesteTesteTesteTesteTesteTesteTesteTesteTeste")

save_model(question)
