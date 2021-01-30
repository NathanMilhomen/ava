from main.app import create_app
from main.app.models.University import UniversityModel
from main.app.utils.models import save_model, delete_model


app = create_app()
app.app_context().push()

uni = UniversityModel('UniEvangelica')
save_model(uni)
