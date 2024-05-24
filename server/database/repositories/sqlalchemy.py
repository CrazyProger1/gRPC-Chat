import sqlalchemy as db

from .types import BaseRepository


class SQLAlchemyRepository(BaseRepository):
    model: db.orm.DeclerativeBase
