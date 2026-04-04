from source.app.main import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(10), nullable=False)
    score = db.Column(db.Integer)
    level = db.Column(db.Integer)

    def __repr__(self):
        return f"<User {self.nickname}>"

    def to_dict(self):
        return {
            "id": self.id,
            "nickname": self.nickname,
            "score": self.score,
            "level": self.level,
        }
