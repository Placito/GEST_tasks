from flask import Blueprint, request, jsonify, redirect, url_for
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from flask_cors import CORS, cross_origin
from api.models import User, db

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