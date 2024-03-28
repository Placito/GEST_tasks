import os
from flask import Flask
from flask_admin import Admin
from .models import Controller, db, User, Seccion_1, Seccion_2, Seccion_3, Seccion_4, Seccion_5, Seccion_6

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'darkly'
    # Include my custom CSS file
    app.config['FLASK_ADMIN_CSS'] = 'front/styles/custom_admin_styles.css'  
    
    admin = Admin(app, name='GEST Admin', template_mode='bootstrap3')

    # Add User model to the admin with an icon
    admin.add_view(Controller(User, db.session))
    # Add Seccion models to the admin with icons and change the display name to "sectors"
    admin.add_view(Controller(Seccion_1, db.session, category='Seccions', name='Sectors 1', menu_icon_type='glyph', menu_icon_value='glyphicon-list-alt'))
    admin.add_view(Controller(Seccion_2, db.session, category='Seccions', name='Sectors 2', menu_icon_type='glyph', menu_icon_value='glyphicon-list-alt'))
    admin.add_view(Controller(Seccion_3, db.session, category='Seccions', name='Sectors 3', menu_icon_type='glyph', menu_icon_value='glyphicon-list-alt'))
    admin.add_view(Controller(Seccion_4, db.session, category='Seccions', name='Sectors 4', menu_icon_type='glyph', menu_icon_value='glyphicon-list-alt'))
    admin.add_view(Controller(Seccion_5, db.session, category='Seccions', name='Sectors 5', menu_icon_type='glyph', menu_icon_value='glyphicon-list-alt'))
    admin.add_view(Controller(Seccion_6, db.session, category='Seccions', name='Sectors 6', menu_icon_type='glyph', menu_icon_value='glyphicon-list-alt'))