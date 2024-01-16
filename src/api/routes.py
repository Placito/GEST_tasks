"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS, cross_origin
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask import session

api = Blueprint('api', __name__)

# Allow CORS requests to this API
cors = CORS(api, resources={r"/api/*": {"origins": "*"}})

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@api.route('/api/token', methods=['POST'])
@cross_origin()
def login_post():
    email = request.json.get('email')
    password = request.json.get('password')

    # Debugging: Print received email and password
    print(f"Received email: {email}")
    print(f"Received password: {password}")

    # Find the user in the database
    user = User.query.filter_by(email=email).first()

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

