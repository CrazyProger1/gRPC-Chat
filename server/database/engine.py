import sqlalchemy as db

from server.config import DATABASE_URI

engine = db.create_engine(DATABASE_URI)
