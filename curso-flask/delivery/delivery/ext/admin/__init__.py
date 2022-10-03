from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from delivery.ext.db import db
from delivery.ext.db.models import Category

admin = Admin()

def init_app(app):
    admin.name = "CodeFoods"
    admin.template_mode = "bootstrap4"
    admin.init_app(app)

    # Proteger com senha

    admin.add_view(ModelView(Category, db.session))
