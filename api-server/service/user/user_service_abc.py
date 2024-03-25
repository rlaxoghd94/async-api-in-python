from abc import ABC, abstractmethod
from typing import List

from domain.user.entity.user import User
from domain.user.model.user import UserModel


class UserServiceABC(ABC):
    @abstractmethod
    async def get_user_with_user_id(self, user_id: int) -> UserModel:
        raise NotImplementedError

    @abstractmethod
    async def get_users_with_user_ids(self, user_ids: List[int]) -> List[UserModel]:
        raise NotImplementedError

    @abstractmethod
    async def register_user(self, user_info: User) -> int:
        raise NotImplementedError

    @abstractmethod
    async def deregister_user_with_user_id(self, user_id: int) -> bool:
        raise NotImplementedError
