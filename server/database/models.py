from datetime import datetime

import sqlalchemy as db


class Base(db.orm.DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    nickname = db.Column(db.String, nullable=False)
    registered_at = db.Column(db.TIMESTAMP, default=datetime.utcnow())
    hashed_password: str = db.Column(db.String(length=1024), nullable=False)
    is_active: bool = db.Column(db.Boolean, default=True, nullable=False)
    is_superuser: bool = db.Column(db.Boolean, default=False, nullable=False)
    is_verified: bool = db.Column(db.Boolean, default=False, nullable=False)
