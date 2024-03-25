from typing import List

from .user_repository_abc import UserRepositoryABC
from domain.user.entity.user import User


class UserRepository(UserRepositoryABC):
    def __init__(self):
        super().__init__(id=int, entity=User)

    async def save(self, entity: User) -> User:
        pass

    async def save_all(self, entities: List[User]) -> List[User]:
        pass

    async def find_by_id(self, id: int):
        pass

    async def exists_by_id(self, id: int) -> bool:
        pass

    async def find_all(self):
        pass

    async def count(self) -> int:
        pass

    async def delete_by_id(self, id: int):
        pass

    async def delete_all_by_id(self, id: int):
        pass

    async def delete(self, entity: User):
        pass

    async def delete_all(self):
        pass
