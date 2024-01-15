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
from flask import session

api = Blueprint('api', __name__)

# Allow CORS requests to this API
cors = CORS(api, resources={r"/api/*": {"origins": "*"}})

mail = Mail()

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
@cross_origin(origin="process.env.FRONTEND_URL")
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
    
    # endpoint for send an email with a link to reset password
@main.route("/resetPassword", methods=["POST"])
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
            link = f"https://silver-cod-gvp74jvvwjqc9vxp-3000.app.github.dev/newPassword?token={token}"

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

