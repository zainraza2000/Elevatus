from common._repositories.base import BaseRepository
from abc import ABCMeta,abstractmethod
from core._models.candidate import Candidate
from typing import List


class CandidateRepository(BaseRepository[Candidate]):
    __metaclass__ = ABCMeta
