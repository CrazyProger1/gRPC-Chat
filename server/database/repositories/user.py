from server.database.models import User
from server.database.repositories.sqlalchemy import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User
