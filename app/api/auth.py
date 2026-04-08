from flask import Blueprint, jsonify, render_template, request
from flask_jwt_extended import create_access_token

from app.config import Config
from app.extensions import db, limiter
from app.models import User
from app.utils import error_response

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login")
def login_page():
    return render_template("login.html")


@auth_bp.route("/api/login", methods=["POST"])
@limiter.limit(Config.LOGIN_LIMITER)
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return error_response("Username and password required")

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return error_response("Invalid username or password", 401)

    access_token = create_access_token(identity=str(user.id))

    return jsonify(access_token=access_token)


@auth_bp.route("/api/register", methods=["POST"])
@limiter.limit(Config.REGISTER_LIMITER)
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return error_response("Username and password required")

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return error_response("Username already exists", 409)

    if (
        len(username) < Config.MIN_USERNAME_LENGTH
        or len(username) > Config.MAX_USERNAME_LENGTH
    ):
        return error_response("Username must be between 3 and 10 characters")
    if len(password) < Config.MIN_PASSWORD_LENGTH:
        return error_response("Password must be at least 6 characters")

    user = User(username=username)  # pyright: ignore[reportCallIssue]
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    access_token = create_access_token(identity=str(user.id))

    return jsonify(access_token=access_token)
