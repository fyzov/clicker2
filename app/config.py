import os

from dotenv import load_dotenv


class Config:
    load_dotenv()

    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "sqlite:///users.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLICK_LIMITER = "35 per minute"
    LOGIN_LIMITER = "5 per hour"
    REGISTER_LIMITER = "1 per hour"
    UPGRADE_LIMITER = "10 per minute"

    BASE_COST = 200
    MULTIPLIER = 1.6
    TOP_LIMIT = 10
    CLICK_PACKAGE_LIMIT = 150
    SQLITE_INTEGER_LIMIT = 2_147_483_647
    MIN_USERNAME_LENGTH = 3
    MAX_USERNAME_LENGTH = 10
    MIN_PASSWORD_LENGTH = 6
