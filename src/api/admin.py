import os
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .models import db, User, Seccion_1, Seccion_2, Seccion_3, Seccion_4, Seccion_5, Seccion_6

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_CSS'] = 'front/styles/admin.css'
    admin = Admin(app, name='GEST Admin', base_template='admin/base.html')

    # Add User and Sector models to the admin interface
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Seccion_1, db.session, category='Sectors', name='Sector 1'))
    admin.add_view(ModelView(Seccion_2, db.session, category='Sectors', name='Sector 2'))
    admin.add_view(ModelView(Seccion_3, db.session, category='Sectors', name='Sector 3'))
    admin.add_view(ModelView(Seccion_4, db.session, category='Sectors', name='Sector 4'))
    admin.add_view(ModelView(Seccion_5, db.session, category='Sectors', name='Sector 5'))
    admin.add_view(ModelView(Seccion_6, db.session, category='Sectors', name='Sector 6'))
