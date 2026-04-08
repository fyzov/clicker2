from flask import Blueprint, redirect, render_template, request, url_for
from flask_jwt_extended import get_jwt_identity, jwt_required, verify_jwt_in_request
from flask_jwt_extended.exceptions import InvalidHeaderError, NoAuthorizationError

from app.config import Config
from app.extensions import db, limiter
from app.models import User
from app.utils import calculate_upgrade_cost, error_response, success_response

game_bp = Blueprint("game", __name__)


@game_bp.route("/")
def index():
    token = request.cookies.get("access_token_cookie") or request.headers.get(
        "Authorization", ""
    ).replace("Bearer ", "")

    if not token:
        return redirect(url_for("auth.login_page"))

    try:
        verify_jwt_in_request()
        return render_template("game.html")
    except (NoAuthorizationError, InvalidHeaderError):
        return redirect(url_for("auth.login_page"))


@game_bp.route("/api/user")
@jwt_required()
def get_user():
    user_id = int(get_jwt_identity())

    user = User.query.get(user_id)
    if not user:
        return error_response(f"User with id {user_id} not found", 404)

    return success_response(user.to_dict())


@game_bp.route("/api/top")
@jwt_required()
def get_top():
    top_users = (
        User.query.with_entities(User.username, User.score)
        .order_by(User.score.desc())
        .limit(Config.TOP_LIMIT)
        .all()
    )

    return success_response(
        [{"username": user.username, "score": user.score} for user in top_users]
    )


@game_bp.route("/api/click", methods=["POST"])
@jwt_required()
@limiter.limit(Config.CLICK_LIMITER)
def click():
    user_id = int(get_jwt_identity())

    data = request.get_json()

    if not data or "clicks" not in data:
        return error_response("Missing 'clicks' field")

    try:
        clicks = int(data.get("clicks"))
        if clicks <= 0 or clicks > Config.CLICK_PACKAGE_LIMIT:
            return error_response("Invalid clicks amount")
    except (TypeError, ValueError):
        return error_response("Clicks must be a number")

    user = User.query.get(user_id)
    if not user:
        return error_response(f"User with id {user_id} not found", 404)

    if user.score + clicks > Config.SQLITE_INTEGER_LIMIT:
        return error_response("Score would exceed maximum limit")

    user.score += clicks * user.level

    db.session.commit()

    return success_response(
        {
            "user_id": user_id,
            "clicks": clicks,
            "message": f"Recorded {clicks} clicks for user {user_id}",
        }
    )


@game_bp.route("/api/upgrade", methods=["POST"])
@jwt_required()
@limiter.limit(Config.UPGRADE_LIMITER)
def upgrade():
    user_id = int(get_jwt_identity())

    user = User.query.get(user_id)
    if not user:
        return error_response(f"User with id {user_id} not found", 404)

    upgrade_cost = calculate_upgrade_cost(user.level + 1)
    if user.score < upgrade_cost:
        return error_response("Not enough score to upgrade")

    user.score -= upgrade_cost
    user.level += 1

    db.session.commit()

    return success_response(
        {
            "user_id": user_id,
            "level": user.level,
            "message": f"Upgraded user {user_id} to level {user.level}",
        }
    )
