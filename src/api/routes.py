"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS, cross_origin
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, \
                               unset_jwt_cookies, jwt_required, JWTManager

api = Blueprint('api', __name__)

# Allow CORS requests to this API
cors = CORS(api, resources={r"/api/*": {"origins": "*"}})

#endpoint for create user
@api.route("/api/create-user", methods=["POST"])
@cross_origin(origin="process.env.FRONTEND_URL")
def create_user():
    data = request.json

    username = data.get("username")
    password = data.get("password")
    print(f"Received password in create_user: {password}")
    name = data.get("name")
    role = data.get("rolee")

    # Validation to check if the username already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"success": "false", "message": "Username already exists"}), 409

    # Hash the password for security
    hashed_password = generate_password_hash(password, method="sha256")

    # Create a new user object
    new_user = User(username=username, password=hashed_password, name=name, role=role)

    # Save the new user object to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"success": "true", "message": "User created successfully"}), 201

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@api.route('/login', methods=['POST'])
@cross_origin()
def login_post():
    username = request.json.get('username')
    password = request.json.get('password')

    # Debugging: Print received username and password
    print(f"Received username: {username}")
    print(f"Received password: {password}")

    # Find the user in the database
    user = User.query.filter_by(username=username).first()

    if user:
        # Debugging: Print stored password hash
        print(f"Stored password hash: {user.password}")

        # Check the password
        if check_password_hash(user.password, password):
            # Debugging: Print success message
            print("Password matches")

            # Create an access token
            access_token = create_access_token(identity=user.id)
            return {"success": "true", "access_token": access_token}
        else:
            # Debugging: Print failure message
            print("Password does not match")
            return {"success": "false", "msg": "Wrong credentials"}
    else:
        # Debugging: Print user not found message
        print("User not found")
        return {"success": "false", "msg": "User not found"}

@api.route("/logout", methods=["POST"])
def logout():
    print("Logout route hit")
    response = jsonify({"success":'true',"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response