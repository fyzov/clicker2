from flask_bcrypt import check_password_hash, generate_password_hash
from flask_login import UserMixin

from app.extensions import db


class User(UserMixin, db.Model):
    __tablename__ = "users"
    __table_args__ = (
        db.Index("idx_score", "score"),
        db.Index("idx_username", "username"),
    )

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), nullable=False)
    score = db.Column(db.Integer, default=0)
    level = db.Column(db.Integer, default=1)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "score": self.score,
            "level": self.level,
        }
