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

    def __init__(self, engine):
        self._engine = engine

    def _get_sqlalchemy_filters(self, **filters):
        yield from (self.get_col(col) == val for col, val in filters.items())

    def _read(self, session, **filters):
        return session.query(self.model).filter(
            *self._get_sqlalchemy_filters(**filters)
        )

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

    def read_by(self, **filters):
        with Session(self._engine) as session:
            logger.info(f"Retrieving object by {filters}")

            instance = self._read(session=session, **filters).first()

            logger.info(f"Object retrieved: {instance}")
            return instance

    def read_many(self, **filters):
        with Session(self._engine) as session:
            logger.info(f"Retrieving objects by {filters}")

            instances = self._read(session=session, **filters)

            logger.info(f"Objects retrieved: {instances}")
            return instances

    def update(self, pk: any, data: dict):
        with Session(self._engine) as session:
            logger.info(f"Updating object {pk}: {data}")

            session.query(self.model).filter(self.get_pk_col() == pk).update(
                {self.get_col(col): val for col, val in data.items()}
            )
            session.commit()

            logger.info(f"Object updated: {data}")

    def delete(self, pk: any):
        with Session(self._engine) as session:
            logger.info(f"Deleting object: {pk}")

            session.query(self.model).filter(self.get_pk_col() == pk).delete()
            session.commit()

            logger.info(f"Object deleted: {pk}")

    def exists(self, **filters) -> bool:
        return self.read_by(**filters) is not None
