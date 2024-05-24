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
            raise AttributeError(f"Column not found {column} at {self.model}")

    def get_pk_col(self) -> db.Column:
        return self.get_col(self.pk_column)

    def create(self, data: dict):
        with Session(self._engine) as session:
            logger.info(f"Inserting object: {data}")
            instance = self.model(**data)
            session.add(instance)
            session.commit()
            getattr(instance, self.pk_column, None)
            logger.info(f"Object inserted: {data}")
            return instance

    def read(self, pk: any):
        with Session(self._engine) as session:
            logger.info(f"Retrieving object by pk: {pk}")
            instance = session.get(self.model, pk)
            logger.info(f"Object retrieved: {instance}")
            return instance

    def read_by(self, column: str, value: any):
        with Session(self._engine) as session:
            logger.info(f"Retrieving object by {column}: {value}")
            instance = (
                session.query(self.model).filter(self.get_col(column) == value).first()
            )
            logger.info(f"Object retrieved: {instance}")
            return instance

    def read_many(self, filters: dict) -> Iterable:
        pass

    def update(self, pk: any, data: dict) -> dict:
        pass

    def delete(self, pk: any):
        pass
