"""
Dependency Injection File
"""
from service.user.user_service import UserService
from domain.user.repository.user_repository import UserRepository


class DependencyInjector:
    user_repository = UserRepository()
    user_service = UserService(user_repository)

    def get_user_service(self) -> UserService:
        return self.user_service


dependency_injector = DependencyInjector()
