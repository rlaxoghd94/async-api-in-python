from typing import List

from domain.user.entity.user import User
from domain.user.model.user import UserModel
from domain.user.repository.user_repository_abc import UserRepositoryABC
from .user_service_abc import UserServiceABC


class UserService(UserServiceABC):
    user_repository: type(UserRepositoryABC)

    def __init__(self, user_repository: type(UserRepositoryABC)):
        self.user_repository = user_repository

    async def get_user_with_user_id(self, user_id: int) -> UserModel:
        user = self.user_repository.find_by_id(id=user_id)
        return UserModel(
            user_id=user_id,
            user_name="nic",
            user_email="nic@nicnic.com",
            user_phone_no="111-222-333"
        )

    async def get_users_with_user_ids(self, user_ids: List[int]) -> List[UserModel]:
        pass

    async def register_user(self, user_info: User) -> int:
        pass

    async def deregister_user_with_user_id(self, user_id: int) -> bool:
        pass
