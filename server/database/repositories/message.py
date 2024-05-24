from server.database.models import Message
from server.database.repositories.sqlalchemy import SQLAlchemyRepository


class MessageRepository(SQLAlchemyRepository):
    model = Message
