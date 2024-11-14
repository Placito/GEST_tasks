import os
from flask import Flask
from asyncio import current_task
from flask_mail import Mail, Message
from flask import Blueprint, request, jsonify, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from flask_cors import CORS, cross_origin
from api.models import User, Seccion_1, Seccion_2, Seccion_3, Seccion_4, Seccion_5, Seccion_6, db
import logging

app = Flask(__name__)

mail = Mail(app)
api = Blueprint('api', __name__)
CORS(api, resources={r"/api/*": {"origins": "*"}})
logging.basicConfig(level=logging.DEBUG)

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
            return jsonify({"success": "false", "msg": "Invalid role assigned to the user"}), 400

        if role == 'director':
            return redirect(url_for('choose_1'))
        elif role == 'administrative':
            return redirect(url_for('choose_2'))
        elif role in ['technician', 'operator', 'quality']:
            return redirect(url_for('choose_3'))

        access_token = create_access_token(identity=user.id, additional_claims={"role": role})

        return jsonify({"success": "true", "access_token": access_token, "role": role}), 200

    else:
        return jsonify({"success": "false", "msg": "Bad username or password"}), 401

# Endpoint to send an email with a link to reset password
@api.route("/resetPassword", methods=["POST"])
@cross_origin(origin=os.getenv("FRONTEND_URL", "*"))
def send_reset_email():
    try:
        if not request.is_json:
            return (
                jsonify(
                    {
                        "error": "415 Unsupported Media Type: Content-Type must be 'application/json'"
                    }
                ),
                415,
            )

        email = request.json.get("email")
        user = User.query.filter_by(email=email).first()

        if user is None:
            return jsonify({"msg": "User with this email does not exist."}), 404
        else:
            token = create_access_token(identity=user.email)
            link = f"https://your_frontend_url/newPassword?token={token}"

            message = Message(
                subject="Password Reset Link",
                sender=app.config["MAIL_USERNAME"],
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

        user = User.query.filter_by(email=email).first()
        if user is None:
            return jsonify({"msg": "User with this email does not exist."}), 404

        user.password = generate_password_hash(password)
        db.session.commit()

        return jsonify({"msg": "Password reset successful."}), 200
    except Exception as e:
        return jsonify({"msg": "An error occurred", "error": str(e)}), 500

# Routes for sectors
@api.route('/sectors', methods=['GET'])
def get_sectors():
    sectors = []
    for section in [Seccion_1, Seccion_2, Seccion_3, Seccion_4, Seccion_5, Seccion_6]:
        sectors.extend(section.query.all())
    return jsonify([sector.serialize() for sector in sectors])

@api.route('/sectors/<int:id>', methods=['GET'])
def get_sector(id):
    for section in [Seccion_1, Seccion_2, Seccion_3, Seccion_4, Seccion_5, Seccion_6]:
        sector = section.query.get(id)
        if sector:
            return jsonify(sector.serialize())
    return jsonify({"msg": "Sector not found"}), 404

@api.route('/sectors', methods=['POST'])
def create_sector():
    data = request.json
    section_class = get_section_class_from_name(data['name'])
    if not section_class:
        return jsonify({"msg": "Invalid sector name"}), 400
    new_sector = section_class(name=data['name'], description=data.get('description'))
    db.session.add(new_sector)
    db.session.commit()
    return jsonify(new_sector.serialize()), 201

@api.route('/sectors/<int:id>', methods=['PUT'])
def update_sector(id):
    data = request.json
    for section in [Seccion_1, Seccion_2, Seccion_3, Seccion_4, Seccion_5, Seccion_6]:
        sector = section.query.get(id)
        if sector:
            sector.name = data.get('name', sector.name)
            sector.description = data.get('description', sector.description)
            db.session.commit()
            return jsonify(sector.serialize())
    return jsonify({"msg": "Sector not found"}), 404

@api.route('/sectors/<int:id>', methods=['DELETE'])
def delete_sector(id):
    for section in [Seccion_1, Seccion_2, Seccion_3, Seccion_4, Seccion_5, Seccion_6]:
        sector = section.query.get(id)
        if sector:
            db.session.delete(sector)
            db.session.commit()
            return jsonify({"success": "true", "msg": "Sector deleted"}), 204
    return jsonify({"msg": "Sector not found"}), 404

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

# Route for logout
@api.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # Here, you can implement token blacklisting if needed
    return jsonify({"success": "true", "msg": "User successfully logged out"}), 200

def get_section_class_from_name(name):
    section_map = {
        'Seccion_1': Seccion_1,
        'Seccion_2': Seccion_2,
        'Seccion_3': Seccion_3,
        'Seccion_4': Seccion_4,
        'Seccion_5': Seccion_5,
        'Seccion_6': Seccion_6,
    }
    return section_map.get(name)
