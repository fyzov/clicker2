from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from model import User

from source.app.util import error_response, get_upgrade_cost, success_response
from source.main import app, click_limit, limiter, top_limit


@app.route("/api/user")
@jwt_required()
def get_user():
    user_id = get_jwt_identity()

    user = User.query.get(user_id)
    if not user:
        return error_response(f"User with id {user_id} not found", 404)

    return success_response(user.to_dict())


@app.route("/api/top")
@jwt_required()
def get_top():
    top_users = User.query.order_by(User.score.desc()).limit(top_limit).all()

    return success_response(
        [{"nickname": user.nickname, "score": user.score} for user in top_users]
    )


@app.route("/api/click", methods=["POST"])
@jwt_required()
@limiter.limit(click_limit)
def click():
    user_id = get_jwt_identity()

    data = request.get_json()

    if not data or "clicks" not in data:
        return error_response("Missing 'clicks' field")

    try:
        clicks = int(data.get("clicks"))
        if clicks <= 0 or clicks > 1000:
            return error_response("Invalid clicks amount")
    except (TypeError, ValueError):
        return error_response("Clicks must be a number")

    user = User.query.get(user_id)
    if not user:
        return error_response(f"User with id {user_id} not found", 404)

    user.score += clicks

    return success_response(
        {
            "user_id": user_id,
            "clicks": clicks,
            "message": f"Recorded {clicks} clicks for user {user_id}",
        }
    )


@app.route("/api/upgrade", methods=["POST"])
@jwt_required()
def upgrade():
    user_id = get_jwt_identity()

    user = User.query.get(user_id)
    if not user:
        return error_response(f"User with id {user_id} not found", 404)

    upgrade_cost = get_upgrade_cost(user.level + 1)
    if user.score < upgrade_cost:
        return error_response({"message": "Not enough score to upgrade"})

    user.score -= upgrade_cost
    user.level += 1

    return success_response(
        {
            "user_id": user_id,
            "level": user.level,
            "message": f"Upgraded user {user_id} to level {user.level}",
        }
    )
