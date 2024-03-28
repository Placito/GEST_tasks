from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, current_user
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for, flash
from flask_admin import expose

db = SQLAlchemy()

# ModelView to protect and define the rights of the users
class Controller(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        flash('You are not authorized to use the admin dashboard', 'error')
        return redirect(url_for('login'))  
   
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "role": self.role,
            # do not serialize the password, its a security breach
        }

class Seccion_1(db.Model):
    __tablename__ = 'seccion_1'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    manufacturer = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    type = db.Column(db.String(100))
    price = db.Column(db.Numeric(precision=10, scale=2))


    def serialize(self):
        return {
        'id': self.id,
        'name': self.name,
        'manufacturer': self.manufacturer,
        'material': self.material,
        'type': self.type,
        'price': str(self.price),  
        }

class Seccion_2(db.Model):
    __tablename__ = 'seccion_2'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    manufacturer = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    type = db.Column(db.String(100))
    price = db.Column(db.Numeric(precision=10, scale=2))


    def serialize(self):
        return {
        'id': self.id,
        'name': self.name,
        'manufacturer': self.manufacturer,
        'material': self.material,
        'type': self.type,
        'price': str(self.price),  
        }

class Seccion_3(db.Model):
    __tablename__ = 'seccion_3'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    manufacturer = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    type = db.Column(db.String(100))
    price = db.Column(db.Numeric(precision=10, scale=2))


    def serialize(self):
        return {
        'id': self.id,
        'name': self.name,
        'manufacturer': self.manufacturer,
        'material': self.material,
        'type': self.type,
        'price': str(self.price),  
        }

class Seccion_4(db.Model):
    __tablename__ = 'seccion_4'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    manufacturer = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    type = db.Column(db.String(100))
    price = db.Column(db.Numeric(precision=10, scale=2))


    def serialize(self):
        return {
        'id': self.id,
        'name': self.name,
        'manufacturer': self.manufacturer,
        'material': self.material,
        'type': self.type,
        'price': str(self.price),  
        }

class Seccion_5(db.Model):
    __tablename__ = 'seccion_5'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    manufacturer = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    type = db.Column(db.String(100))
    price = db.Column(db.Numeric(precision=10, scale=2))


    def serialize(self):
        return {
        'id': self.id,
        'name': self.name,
        'manufacturer': self.manufacturer,
        'material': self.material,
        'type': self.type,
        'price': str(self.price),  
        }

class Seccion_6(db.Model):
    __tablename__ = 'seccion_6'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    manufacturer = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    type = db.Column(db.String(100))
    price = db.Column(db.Numeric(precision=10, scale=2))


    def serialize(self):
        return {
        'id': self.id,
        'name': self.name,
        'manufacturer': self.manufacturer,
        'material': self.material,
        'type': self.type,
        'price': str(self.price),  
        }
