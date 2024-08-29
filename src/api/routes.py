from flask import Blueprint, request, jsonify, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from flask_cors import CORS, cross_origin
from api.models import User, Seccion_1, Seccion_2, Seccion_3, Seccion_4, Seccion_5, Seccion_6,  db

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
    # Retrieve username and password from the request
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Query the user by username
    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        role = user.role

        # Validate the role
        if role not in ROLES:
            return jsonify({"success": "false", "msg": "Invalid role assigned to the user"}), 400

        # Redirect based on role
        if role == 'director':
            return redirect(url_for('choose_1'))
        elif role == 'administrative':
            return redirect(url_for('choose_2'))
        elif role in ['technician', 'operator', 'quality']:
            return redirect(url_for('choose_3'))

        # Create access token with role information
        access_token = create_access_token(identity=user.id, additional_claims={"role": role})

        # Respond with success, token, and role
        return jsonify({"success": "true", "access_token": access_token, "role": role}), 200

    else:
        # Respond with error if username or password is incorrect
        return jsonify({"success": "false", "msg": "Bad username or password"}), 401


# Routes for sectors
@api.route('/sectors', methods=['GET'])
def get_sectors():
    sectors = [Seccion_1, Seccion_2, Seccion_3, Seccion_4, Seccion_5, Seccion_6].query.all()
    return jsonify([sector.serialize() for sector in sectors])

@api.route('/sectors/<int:id>', methods=['GET'])
def get_sector(id):
    sectors = [Seccion_1, Seccion_2, Seccion_3, Seccion_4, Seccion_5, Seccion_6].query.all()
    return jsonify(sectors.serialize())

@api.route('/sectors', methods=['POST'])
def create_sector():
    data = request.json
    new_sector = [Seccion_1, Seccion_2, Seccion_3, Seccion_4, Seccion_5, Seccion_6](name=data['name'], description=data.get('description'))
    db.session.add(new_sector)
    db.session.commit()
    return jsonify(new_sector.serialize()), 201

@api.route('/sectors/<int:id>', methods=['PUT'])
def update_sector(id):
    sectors = [Seccion_1, Seccion_2, Seccion_3, Seccion_4, Seccion_5, Seccion_6].query.all()
    data = request.json
    sectors.name = data.get('name', sectors.name)
    sectors.description = data.get('description', sectors.description)
    db.session.commit()
    return jsonify(sectors.serialize())

@api.route('/sectors/<int:id>', methods=['DELETE'])
def delete_sector(id):
    sectors = [Seccion_1, Seccion_2, Seccion_3, Seccion_4, Seccion_5, Seccion_6].query.all()
    db.session.delete(sectors)
    db.session.commit()
    return jsonify({"success": "true", "msg": "Sector deleted"}), 204


# Routes for users
@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users])

@api.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.serialize())

@api.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'], password=generate_password_hash(data['password']))
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize()), 201

@api.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.json
    user.username = data.get('username', user.username)
    if 'password' in data:
        user.password = generate_password_hash(data['password'])
    db.session.commit()
    return jsonify(user.serialize())

@api.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"success": "true", "msg": "User deleted"}), 204

#route for logout
@api.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # Here, you can implement token blacklisting if needed
    return jsonify({"success": "true", "msg": "User successfully logged out"}), 200