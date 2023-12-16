from abc import ABCMeta, abstractmethod
from typing import Optional, List, TypeVar, Generic

T = TypeVar("T")

class BaseRepository(Generic[T]):
    __metaclass__ = ABCMeta

    @abstractmethod
    async def find(self, query) -> Optional[T]:
        pass
    
    @abstractmethod
    async def find_one(self, query) -> List[T]:
        pass

    @abstractmethod
    async def get_by_id(self, id: int | str) -> Optional[T]:
        pass

    @abstractmethod
    async def get_all(self) -> List[T]:
        pass

    @abstractmethod
    async def create(self, item: T) -> T:
        pass

    @abstractmethod
    async def update(self,id: int | str, item: T) -> None:
        pass

    @abstractmethod
    async def delete(self, item: T) -> None:
        pass

