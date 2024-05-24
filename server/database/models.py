from datetime import datetime

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

metadata = db.MetaData()
Base = declarative_base(metadata=metadata)


class User(Base):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    nickname = db.Column(db.String, nullable=False)
    registered_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    hashed_password = db.Column(db.String(length=1024), nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    is_superuser = db.Column(db.Boolean, default=False, nullable=False)
    is_verified = db.Column(db.Boolean, default=False, nullable=False)

    messages_sent = relationship("Message", back_populates="sender")
    messages_received = relationship("Message", back_populates="receiver")


class Message(Base):
    __tablename__ = "message"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    sender = relationship("User", back_populates="messages_sent")
    receiver = relationship("User", back_populates="messages_received")
