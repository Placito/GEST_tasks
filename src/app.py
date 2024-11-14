import os
from flask import Flask, jsonify, send_from_directory, redirect, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from api.utils import APIException, generate_sitemap
from api.models import db, User
from api.routes import api
from api.admin import setup_admin
from api.commands import setup_commands
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_login import LoginManager

ENV = "development" if os.getenv("FLASK_DEBUG") == "1" else "production"
static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')

app = Flask(__name__, template_folder="templates")

app.url_map.strict_slashes = False
login_manager = LoginManager()
login_manager.init_app(app)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET')
jwt = JWTManager(app)

# Initialize CORS
frontend_url = os.getenv("FRONTEND_URL")
CORS(app, origins=[frontend_url] if frontend_url else "*")

# database configuration
db_url = os.getenv("DATABASE_URL", "sqlite:////tmp/test.db")
app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Migrate(app, db, compare_type=True)
db.init_app(app)

# Add the admin interface
setup_admin(app)

# Add custom commands
setup_commands(app)

# Register API endpoints
app.register_blueprint(api, url_prefix='/api')

# Handle/serialize errors as JSON objects
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Redirect from root URL to /admin/
@app.route('/')
def root_to_admin():
    """Redirect root URL to /admin/"""
    return redirect(url_for('admin.index'))

# Generate sitemap with all endpoints for development environment
@app.route('/sitemap')
def sitemap():
    """Generate a sitemap with all endpoints."""
    if ENV == "development":
        return generate_sitemap(app)
    return send_from_directory(static_file_dir, 'index.html')

# Serve any other file as a static file
@app.route('/<path:path>', methods=['GET'])
def serve_any_other_file(path):
    """Serve any other file as a static file."""
    if not os.path.isfile(os.path.join(static_file_dir, path)):
        path = 'index.html'
    response = send_from_directory(static_file_dir, path)
    response.cache_control.max_age = 0  # Avoid caching
    return response

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Unauthorized handler
@login_manager.unauthorized_handler
def unauthorized_handler():
    return jsonify({"success": "false", "msg": "Unauthorized"}), 401

# Run the app if executed directly
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3001))
    db.create_all()
    app.run(host='0.0.0.0', port=PORT, debug=True)
