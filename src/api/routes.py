from os import abort
import sys
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flask_jwt_extended import create_access_token, unset_jwt_cookies, jwt_required
from api.models import Seccion_1, Seccion_2, Seccion_3, Seccion_4, Seccion_5, Seccion_6, db, User
from flask_cors import CORS, cross_origin

api = Blueprint('api', __name__)
CORS(api, resources={r"/api/*": {"origins": "*"}})

# Roles dictionary
ROLES = {
    'director': ['director'],
    'administrative': ['administrative'],
    'technician': ['technician'],
    'operator': ['operator'],
    'quality': ['quality'],
}

# Login route 
@api.route('/login', methods=['POST'])
@cross_origin()
def login_post():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        role = user.role
        if role not in ROLES:
            return {"success": "false", "msg": "Invalid role assigned to the user"}, 400
        access_token = create_access_token(identity=user.id, additional_claims={"role": role})
        return {"success": "true", "access_token": access_token, "role": role}, 200
    else:
        return {"success": "false", "msg": "Bad username or password"}, 401

# Logout route
@api.route('/logout', methods=['POST'])
@login_required
@cross_origin()
def logout():
    response = jsonify({"success": "true", "msg": "logout successful"})
    unset_jwt_cookies(response)
    return response, 200

# User creation route
@api.route('/create-user', methods=['POST'])
@cross_origin()
def create_user():
    username = request.json.get('username', None)
    name = request.json.get('name', None)
    role = request.json.get('role', None)
    password = request.json.get('password', None)

    if User.query.filter_by(username=username).first():
        return jsonify({'success': 'false', 'msg': "user already exists"}), 409

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256:20000')
    new_user = User(username=username, name=name, role=role, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    access_token = create_access_token(identity=new_user.id)
    return jsonify({'success': 'true', "access_token": access_token}), 201

# route for director
@api.route('/director', methods=['GET'])
@login_required.role('director')
def director():
    error = False
    body = {}
    try:
        # Fetch all sections
        seccion_1 = [sec.serialize() for sec in Seccion_1.query.all()]
        seccion_2 = [sec.serialize() for sec in Seccion_2.query.all()]
        seccion_3 = [sec.serialize() for sec in Seccion_3.query.all()]
        seccion_4 = [sec.serialize() for sec in Seccion_4.query.all()]
        seccion_5 = [sec.serialize() for sec in Seccion_5.query.all()]
        seccion_6 = [sec.serialize() for sec in Seccion_6.query.all()]

        # Combine all sections into the response body
        body['seccion_1'] = seccion_1
        body['seccion_2'] = seccion_2
        body['seccion_3'] = seccion_3
        body['seccion_4'] = seccion_4
        body['seccion_5'] = seccion_5
        body['seccion_6'] = seccion_6

    except Exception as e:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return jsonify(body)

# route for administrative, can create users, view, edit and delete 
@api.route('/administrative', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required.role('administrative')
def administrative():
    error = False
    body = {}

    try:
        if request.method == 'GET':
            # Fetch all sections
            seccion_1 = [sec.serialize() for sec in Seccion_1.query.all()]
            seccion_2 = [sec.serialize() for sec in Seccion_2.query.all()]
            seccion_3 = [sec.serialize() for sec in Seccion_3.query.all()]
            seccion_4 = [sec.serialize() for sec in Seccion_4.query.all()]
            seccion_5 = [sec.serialize() for sec in Seccion_5.query.all()]
            seccion_6 = [sec.serialize() for sec in Seccion_6.query.all()]

            # Combine all sections into the response body
            body['seccion_1'] = seccion_1
            body['seccion_2'] = seccion_2
            body['seccion_3'] = seccion_3
            body['seccion_4'] = seccion_4
            body['seccion_5'] = seccion_5
            body['seccion_6'] = seccion_6

            # Fetch all users
            users = [user.serialize() for user in User.query.all()]
            body['users'] = users

        elif request.method == 'POST':
            # Create a new user
            data = request.get_json()
            new_user = User(
                username=data['username'],
                email=data['email'],
                role=data['role'],
                password=generate_password_hash(data['password'], method='pbkdf2:sha256:20000')
            )
            db.session.add(new_user)
            db.session.commit()
            body['message'] = 'User created successfully.'

        elif request.method == 'PUT':
            # Update an existing user
            data = request.get_json()
            user = User.query.get(data['id'])
            if user:
                user.username = data['username']
                user.email = data['email']
                user.role = data['role']
                if 'password' in data:
                    user.password = generate_password_hash(data['password'], method='pbkdf2:sha256:20000')
                db.session.commit()
                body['message'] = 'User updated successfully.'
            else:
                error = True
                body['message'] = 'User not found.'

        elif request.method == 'DELETE':
            # Delete a user
            data = request.get_json()
            user = User.query.get(data['id'])
            if user:
                db.session.delete(user)
                db.session.commit()
                body['message'] = 'User deleted successfully.'
            else:
                error = True
                body['message'] = 'User not found.'

    except Exception as e:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()

    if error:
        abort(500)
    else:
        return jsonify(body)

# route for technician, can view, edit and delete 
@api.route('/technician/table_sectors', methods=['GET', 'PUT', 'DELETE'])
@login_required.role('technician')
def technician_sectores():
    error = False
    body = {}

    try:
        if request.method == 'GET':
            # Fetch all sections
            seccion_1 = [sec.serialize() for sec in Seccion_1.query.all()]
            seccion_2 = [sec.serialize() for sec in Seccion_2.query.all()]
            seccion_3 = [sec.serialize() for sec in Seccion_3.query.all()]
            seccion_4 = [sec.serialize() for sec in Seccion_4.query.all()]
            seccion_5 = [sec.serialize() for sec in Seccion_5.query.all()]
            seccion_6 = [sec.serialize() for sec in Seccion_6.query.all()]

            # Combine all sections into the response body
            body['seccion_1'] = seccion_1
            body['seccion_2'] = seccion_2
            body['seccion_3'] = seccion_3
            body['seccion_4'] = seccion_4
            body['seccion_5'] = seccion_5
            body['seccion_6'] = seccion_6

        elif request.method == 'PUT':
            # Update a specific sector (section)
            data = request.get_json()
            section_id = data.get('id')
            section_table = data.get('section_table')

            # Get the correct section table model
            section_model = globals().get(section_table)

            if section_model:
                section = section_model.query.get(section_id)
                if section:
                    section.name = data.get('name', section.name)
                    section.manufacturer = data.get('manufacturer', section.manufacturer)
                    section.gender = data.get('gender', section.gender)
                    section.type = data.get('type', section.type)
                    section.price = data.get('price', section.price)
                    db.session.commit()
                    body['message'] = 'Section updated successfully.'
                else:
                    error = True
                    body['message'] = 'Section not found.'
            else:
                error = True
                body['message'] = 'Invalid section table.'

        elif request.method == 'DELETE':
            # Delete a specific sector (section)
            data = request.get_json()
            section_id = data.get('id')
            section_table = data.get('section_table')

            # Get the correct section table model
            section_model = globals().get(section_table)

            if section_model:
                section = section_model.query.get(section_id)
                if section:
                    db.session.delete(section)
                    db.session.commit()
                    body['message'] = 'Section deleted successfully.'
                else:
                    error = True
                    body['message'] = 'Section not found.'
            else:
                error = True
                body['message'] = 'Invalid section table.'

    except Exception as e:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()

    if error:
        abort(500)
    else:
        return jsonify(body)

# route for operator, can view, edit and delete 
@api.route('/operator/table_sectors', methods=['GET', 'PUT', 'DELETE'])
@login_required.role('operator')
def operator_sectores():
    error = False
    body = {}

    try:
        if request.method == 'GET':
            # Fetch all sections
            seccion_1 = [sec.serialize() for sec in Seccion_1.query.all()]
            seccion_2 = [sec.serialize() for sec in Seccion_2.query.all()]
            seccion_3 = [sec.serialize() for sec in Seccion_3.query.all()]
            seccion_4 = [sec.serialize() for sec in Seccion_4.query.all()]
            seccion_5 = [sec.serialize() for sec in Seccion_5.query.all()]
            seccion_6 = [sec.serialize() for sec in Seccion_6.query.all()]

            # Combine all sections into the response body
            body['seccion_1'] = seccion_1
            body['seccion_2'] = seccion_2
            body['seccion_3'] = seccion_3
            body['seccion_4'] = seccion_4
            body['seccion_5'] = seccion_5
            body['seccion_6'] = seccion_6

        elif request.method == 'PUT':
            # Update a specific sector (section)
            data = request.get_json()
            section_id = data.get('id')
            section_table = data.get('section_table')

            # Get the correct section table model
            section_model = globals().get(section_table)

            if section_model:
                section = section_model.query.get(section_id)
                if section:
                    section.name = data.get('name', section.name)
                    section.manufacturer = data.get('manufacturer', section.manufacturer)
                    section.gender = data.get('gender', section.gender)
                    section.type = data.get('type', section.type)
                    section.price = data.get('price', section.price)
                    db.session.commit()
                    body['message'] = 'Section updated successfully.'
                else:
                    error = True
                    body['message'] = 'Section not found.'
            else:
                error = True
                body['message'] = 'Invalid section table.'

        elif request.method == 'DELETE':
            # Delete a specific sector (section)
            data = request.get_json()
            section_id = data.get('id')
            section_table = data.get('section_table')

            # Get the correct section table model
            section_model = globals().get(section_table)

            if section_model:
                section = section_model.query.get(section_id)
                if section:
                    db.session.delete(section)
                    db.session.commit()
                    body['message'] = 'Section deleted successfully.'
                else:
                    error = True
                    body['message'] = 'Section not found.'
            else:
                error = True
                body['message'] = 'Invalid section table.'

    except Exception as e:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()

    if error:
        abort(500)
    else:
        return jsonify(body)

# route for quality, can view, edit and delete 
@api.route('/quality/table_sectors', methods=['GET', 'PUT', 'DELETE'])
@login_required.role('quality')
def quality_sectores():
    error = False
    body = {}

    try:
        if request.method == 'GET':
            # Fetch all sections
            seccion_1 = [sec.serialize() for sec in Seccion_1.query.all()]
            seccion_2 = [sec.serialize() for sec in Seccion_2.query.all()]
            seccion_3 = [sec.serialize() for sec in Seccion_3.query.all()]
            seccion_4 = [sec.serialize() for sec in Seccion_4.query.all()]
            seccion_5 = [sec.serialize() for sec in Seccion_5.query.all()]
            seccion_6 = [sec.serialize() for sec in Seccion_6.query.all()]

            # Combine all sections into the response body
            body['seccion_1'] = seccion_1
            body['seccion_2'] = seccion_2
            body['seccion_3'] = seccion_3
            body['seccion_4'] = seccion_4
            body['seccion_5'] = seccion_5
            body['seccion_6'] = seccion_6

        elif request.method == 'PUT':
            # Update a specific sector (section)
            data = request.get_json()
            section_id = data.get('id')
            section_table = data.get('section_table')

            # Get the correct section table model
            section_model = globals().get(section_table)

            if section_model:
                section = section_model.query.get(section_id)
                if section:
                    section.name = data.get('name', section.name)
                    section.manufacturer = data.get('manufacturer', section.manufacturer)
                    section.gender = data.get('gender', section.gender)
                    section.type = data.get('type', section.type)
                    section.price = data.get('price', section.price)
                    db.session.commit()
                    body['message'] = 'Section updated successfully.'
                else:
                    error = True
                    body['message'] = 'Section not found.'
            else:
                error = True
                body['message'] = 'Invalid section table.'

        elif request.method == 'DELETE':
            # Delete a specific sector (section)
            data = request.get_json()
            section_id = data.get('id')
            section_table = data.get('section_table')

            # Get the correct section table model
            section_model = globals().get(section_table)

            if section_model:
                section = section_model.query.get(section_id)
                if section:
                    db.session.delete(section)
                    db.session.commit()
                    body['message'] = 'Section deleted successfully.'
                else:
                    error = True
                    body['message'] = 'Section not found.'
            else:
                error = True
                body['message'] = 'Invalid section table.'

    except Exception as e:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()

    if error:
        abort(500)
    else:
        return jsonify(body)
