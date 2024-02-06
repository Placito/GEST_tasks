from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, jsonify, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS, cross_origin
from functools import wraps
from flask_jwt_extended import create_access_token, unset_jwt_cookies, jwt_required, JWTManager

api = Blueprint('api', __name__)

# Allow CORS requests to this API
cors = CORS(api, resources={r"/api/*": {"origins": "*"}})

# Define roles 
ROLES = {
    'director': ['director'],
    'administrative': ['administrative'],
    'technician': ['technician'],
    'operator': ['operator'],
    'quality': ['quality'],
}

# Create a route to authenticate your users and return JWTs.
@api.route('/login', methods=['POST'])
@cross_origin()
def login_post():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()

    if user:
        if check_password_hash(user.password, password):
            access_token = create_access_token(identity=user.id)
            return {"success": "true", "access_token": access_token}
        else:
            return {"success": "false", "msg": "Wrong credentials"}
    else:
        return {"success": "false", "msg": "User not found"}

# Create a route to log out users
@api.route("/logout", methods=["POST"])
@cross_origin()
def logout():
    print("Logout route hit")
    response = jsonify({"success": 'true', "msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

@api.route('/create-user', methods=['POST'])
@cross_origin()
def create_user():
    username = request.json.get('username')
    name = request.json.get('name')
    role = request.json.get('role')
    password = request.json.get('password')
    
    # Debugging: print received password
    print(f"Received password during signup: {password}")

    # Check if user already exists
    user = User.query.filter_by(username=username).first()
    if user:
        return {'success': 'false', 'msg': "user already exists"}

    # Hash the password using PBKDF2 with SHA-256 and 20,000 iterations
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256:20000')
    
    # Debugging: print hashed password
    print(f"Hashed password: {hashed_password}")

    # Create the new user
    new_user = User(username=username, name=name, role=role, password=hashed_password)

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    # Create access token
    user = User.query.filter_by(username=username).first()
    access_token = create_access_token(identity=user.id)

    return {'success': 'true', "access_token": access_token}
