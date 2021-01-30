from main.app.models.Subject import SubjectModel
from main.app.utils.test_model import get_application
from main.app.utils.models import save_model

get_application()

subject = SubjectModel('Lógica de Programação', 80.0, 20)

save_model(subject)
