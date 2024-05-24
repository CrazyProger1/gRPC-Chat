import logging
from typing import Iterable

import sqlalchemy as db
from sqlalchemy.orm import Session

from server.database.models import Base
from server.database.repositories.types import BaseRepository

logger = logging.getLogger("chat")


class SQLAlchemyRepository(BaseRepository):
    model: Base
    pk_column: str = "id"

    def __init__(self, engine: db.Engine):
        self._engine = engine

    def get_col(self, column: str) -> db.Column:
        try:
            return getattr(self.model, column)
        except AttributeError:
            logger.info(f"Column not found {column} at {self.model}")
            raise AttributeError(
                f"Column not found {column} at {self.model}"
            )

    def get_pk_col(self) -> db.Column:
        return self.get_col(self.pk_column)

    def execute(self, session, stmt):
        logger.info(f"SQL: {stmt}")
        try:
            result = session.execute(stmt)
            logger.info(f"SQL executed successfully: {stmt}")
            return result
        except Exception as e:
            logger.error(f"Error executing SQL: {type(e).__name__}: {e}")
            raise

    def create(self, data: dict) -> dict:
        result_data = data.copy()
        with Session(self._engine) as session:
            stmt = db.insert(self.model).values(**data).returning(self.get_pk_col())
            result = self.execute(session=session, stmt=stmt)
            pk = result.scalar_one()
            session.commit()
            result_data.update({self.pk_column: pk})
            return result_data

    def read(self, pk: any):
        with Session(self._engine) as session:
            stmt = db.select(self.model).where(self.get_pk_col() == pk)
            result = self.execute(session=session, stmt=stmt).first()
            if result:
                return result[0]

    def read_by(self, column: str, value: any):
        with Session(self._engine) as session:
            stmt = db.select(self.model).where(self.get_col(column) == value)
            result = self.execute(session=session, stmt=stmt).first()
            if result:
                return result[0]

    def read_many(self, filters: dict) -> Iterable:
        pass

    def update(self, pk: any, data: dict) -> dict:
        pass

    def delete(self, pk: any):
        pass
