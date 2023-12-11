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
from flask_mail import Mail, Message, current_app

api = Blueprint('api', __name__)

mail = Mail()

# Allow CORS requests to this API
CORS(api)
cors = CORS(api, resources={r"/api/*": {"origins": "*"}})

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@api.route("/token", methods=["POST"])
@cross_origin()
def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# endpoint for send an email with a link to reset password
@api.route("/resetPassword", methods=["POST"])
@cross_origin(origin="process.env.FRONTEND_URL")
def send_reset_email():
    try:
        # Ensure that the request has the correct Content-Type header
        if request.headers["Content-Type"] != "application/json":
            return (
                jsonify(
                    {
                        "error": "415 Unsupported Media Type: Content-Type must be 'application/json'"
                    }
                ),
                415,
            )

        email = request.json.get("email")
        print(email)

        # Query the database to check if the email exists
        user = User.query.filter_by(email=email).first()
        print(user)

        if user is None:
            return jsonify({"msg": "User with this email does not exist."}), 404
        else:
            # Generate an access token and construct the reset link
            token = create_access_token(identity=user.email)
            link = f"https://humble-bassoon-q5xp7j55gjgh6wwj-3000.app.github.dev/newPassword?token={token}"

            message = Message(
                subject="Password Reset Link",
                sender=current_app.config["MAIL_USERNAME"],
                recipients=[email],
                body="Hey, this is a link for resetting the password.",
                html=f"Reset your password with this link: <a href='{link}'>Reset Password</a>",
            )

            mail.send(message)
            return jsonify({"message": "Password reset email sent successfully"}), 200
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500

# Endpoint for updating the password
@api.route("/newPassword", methods=["POST"])
@jwt_required()
@cross_origin()
def reset_password():
    try:
        password = request.json.get("password", None)
        email = get_jwt_identity()

        # Query the database to check if the email exists
        user = User.query.filter_by(email=email).first()
        if user is None:
            return jsonify({"msg": "User with this email does not exist."}), 404
        # Update the user's password
        User.password = password
        print(User.password)
        # Commit the changes to the database
        db.session.commit()

        return jsonify({"msg": "Password reset successful."}), 200
    except Exception as e:
        return jsonify({"msg": "An error occurred", "error": str(e)}), 500