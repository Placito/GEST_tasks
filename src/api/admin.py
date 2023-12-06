  
import os
from flask_admin import Admin
from .models import db, User, Seccion_1, Seccion_2, Seccion_3, Seccion_4, Seccion_5, Seccion_6
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add User model to the admin
    admin.add_view(ModelView(User, db.session))
    # Add Seccion model to the admin
    admin.add_view(ModelView(Seccion_1, db.session))
    admin.add_view(ModelView(Seccion_2, db.session))
    admin.add_view(ModelView(Seccion_3, db.session))
    admin.add_view(ModelView(Seccion_4, db.session))
    admin.add_view(ModelView(Seccion_5, db.session))
    admin.add_view(ModelView(Seccion_6, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))