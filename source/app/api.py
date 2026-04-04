from main import app
from model import User
from flask import jsonify


@app.route("/api/user/<int:id>")
def get_user(id):
    user = User.query.get_or_404(id, description=f"User with id {id} not found")

    return jsonify(user.to_dict())


@app.route("/api/top/<limit:int>")
def get_top(limit):
    top_users = User.query.order_by(User.score.desc()).limit(limit).all()

    return jsonify(
        [{"nickname": user.nickname, "score": user.score} for user in top_users]
    )
