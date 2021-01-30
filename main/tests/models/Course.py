from main.app import create_app
from main.app.models.Course import CourseModel
from main.app.utils.models import save_model, delete_model


app = create_app()
app.app_context().push()

engineering = CourseModel('Engineering')
save_model(engineering)
