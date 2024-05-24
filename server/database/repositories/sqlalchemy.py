import logging
from typing import Iterable

import sqlalchemy as db

from server.database.models import Base
from server.database.repositories.types import BaseRepository

logger = logging.getLogger("chat")


class SQLAlchemyRepository(BaseRepository):
    model: Base
    pk_column: str = "id"

    def __init__(self, engine: db.Engine):
        self._engine = engine

    def get_pk_col(self):
        try:
            return getattr(self.model, self.pk_column)
        except AttributeError:
            logger.info(f"PK column not found {self.pk_column} at {self.model}")
            raise AttributeError(f"PK column not found {self.pk_column} at {self.model}")

    def execute(self, stmt):
        logger.info(f"SQL: {stmt}")

        with self._engine.connect() as connection:
            results = connection.execute(statement=stmt)
            connection.commit()
            return results

    def create(self, data: dict) -> dict:
        result_data = data.copy()
        stmt = db.insert(self.model).values(**data).returning(self.get_pk_col())
        result = self.execute(stmt=stmt)
        result_data.update({self.pk_column: result.scalar_one()})
        return result_data

    def read(self, pk: any):
        pass

    def read_many(self, filters: dict) -> Iterable:
        pass

    def update(self, pk: any, data: dict) -> dict:
        pass

    def delete(self, pk: any):
        pass
