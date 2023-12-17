from common._repositories.base import BaseRepository
from abc import ABCMeta,abstractmethod
from core._models.user import User
from typing import List

#abstract class for implementing user specific repository actions
class UserRepository(BaseRepository[User]):
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_by_email(self, email: str) -> User:
        pass