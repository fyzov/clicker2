from flask import Flask

from .api import auth_bp, game_bp
from .config import Config
from .extensions import bcrypt, db, jwt, limiter
from .models import User
from .utils import (
    calculate_upgrade_cost,
    clear_upgrade_cache,
    error_response,
    success_response,
)


def create_app(config=Config):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = config.SECRET_KEY
    app.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS

    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    limiter.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(game_bp)

    clear_upgrade_cache()

    with app.app_context():
        db.create_all()

    return app
