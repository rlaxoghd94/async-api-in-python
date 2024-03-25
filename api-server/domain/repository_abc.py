from typing import List
from abc import ABC, abstractmethod


class RepositoryABC(ABC):
    """
    Base repository class

    Note:
        Since python uses duck typing, generics are not needed; therefore,
        take in pk and entity object as constructor param
    """

    def __init__(self, id, entity):
        self.id = id
        self.entity = entity
        super().__init__()

    @abstractmethod
    async def save(self, entity) -> object:
        raise NotImplementedError

    @abstractmethod
    async def save_all(self, entities) -> List[object]:
        raise NotImplementedError

    @abstractmethod
    async def find_by_id(self, id):
        raise NotImplementedError

    @abstractmethod
    async def exists_by_id(self, id) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError

    @abstractmethod
    async def count(self) -> int:
        raise NotImplementedError

    @abstractmethod
    async def delete_by_id(self, id):
        raise NotImplementedError

    @abstractmethod
    async def delete_all_by_id(self, id):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, entity):
        raise NotImplementedError

    @abstractmethod
    async def delete_all(self):
        raise NotImplementedError
