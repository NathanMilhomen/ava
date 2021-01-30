from main.app.models.Quiz import QuizModel
from main.app.models.Question import QuestionModel
from main.app.utils.test_model import get_application
from main.app.utils.models import save_model

from datetime import datetime

tomorrow = datetime.strptime('28/01/2021 23:59:59', '%d/%m/%Y %H:%M:%S')
get_application()

quiz = QuizModel(datetime.now(), tomorrow, 10, 10, 1, '77766655511')
question = QuestionModel.query.first()
quiz.questions.append(question)
save_model(quiz)
