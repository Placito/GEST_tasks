from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flask_jwt_extended import create_access_token, unset_jwt_cookies, jwt_required
from api.models import db, User
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