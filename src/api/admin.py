import os
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import Controller
from .models import db, User, Seccion_1, Seccion_2, Seccion_3, Seccion_4, Seccion_5, Seccion_6

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_CSS'] = 'front/styles/custom_admin_styles.css'
    admin = Admin(app, name='GEST Admin', base_template='admin/base.html')

    admin = Admin(app, name='GEST Admin', base_template='admin/base.html')  # Ensure this points to your custom base template

    # Add User model to the admin with an icon
    admin.add_view(Controller(User, db.session))
    # Add Seccion models to the admin with icons
    admin.add_view(Controller(Seccion_1, db.session, category='Sectors', name='Sector 1'))
    admin.add_view(Controller(Seccion_2, db.session, category='Sectors', name='Sector 2'))
    admin.add_view(Controller(Seccion_3, db.session, category='Sectors', name='Sector 3'))
    admin.add_view(Controller(Seccion_4, db.session, category='Sectors', name='Sector 4'))
    admin.add_view(Controller(Seccion_5, db.session, category='Sectors', name='Sector 5'))
    admin.add_view(Controller(Seccion_6, db.session, category='Sectors', name='Sector 6'))
