from common._repositories.base import BaseRepository
from abc import ABCMeta,abstractmethod
from core._models.candidate import Candidate
from typing import List

#abstract class for implementing candidate specific repository actions
class CandidateRepository(BaseRepository[Candidate]):
    __metaclass__ = ABCMeta
