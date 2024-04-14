"""
Dependency Injection File
"""
from typing import Generator

from domain.user.repository.user_repository import UserRepository
from infrastructure.database.database_abc import DatabaseABC
from infrastructure.database.rdbms.mysql import MySQLDatabase
from service.user.user_service import UserService


class DependencyInjector:
    user_repository = UserRepository()
    user_service = UserService(user_repository)
    database_source: DatabaseABC = MySQLDatabase()

    def get_user_service(self) -> UserService:
        return self.user_service

    def get_database(self) -> Generator:
        db = self.database_source.get_db_session()
        db.current_user_id = None
        try:
            yield db
        finally:
            db.close()


dependency_injector = DependencyInjector()
