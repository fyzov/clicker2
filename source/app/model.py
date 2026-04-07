from source.main import db


class User(db.Model):
    __tablename__ = "users"
    __table_args__ = (db.Index("idx_score", "score"),)
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(10), nullable=False)
    score = db.Column(db.Integer, default=0)
    level = db.Column(db.Integer, default=1)

    def to_dict(self):
        return {
            "id": self.id,
            "nickname": self.nickname,
            "score": self.score,
            "level": self.level,
        }
