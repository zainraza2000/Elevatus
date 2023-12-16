from typing import List
from core._repositories.abstract.candidate import CandidateRepository
from core._models.candidate import Candidate
from db.mongo import get_mongodb
from pymongo import ReturnDocument
from bson import ObjectId
from core.candidate.dtos.request import CandidateUpdate

class CandidateMongoRepository(CandidateRepository):
    def __init__(self) -> None:
        super().__init__()
        self.db = get_mongodb()

    async def find(self, query) -> List[Candidate]:
        return list(self.db.candidate.find(query))
    
    async def find_one(self, query) -> List[Candidate]:
        return list(self.db.candidate.find_one(query))

    async def get_all(self) -> List[Candidate]:
        can = list(self.db.candidate.find())
        candidates = [Candidate.model_validate(item) for item in can]
        return candidates
    
    async def get_by_id(self, id: str) -> Candidate | None:
        return self.db.candidate.find_one({"_id": ObjectId(id)})
    
    async def create(self,candidate: Candidate) -> Candidate | None:
        new_candidate = self.db.candidate.insert_one(candidate.model_dump(by_alias=True, exclude=["uuid"]))
        created_candidate = self.db.candidate.find_one(
            {"_id": new_candidate.inserted_id}
        )
        return created_candidate
    
    async def update(self, id: int | str, item: CandidateUpdate) -> None:
        return self.db.candidate.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": item.model_dump(by_alias=True, exclude=["uuid"])},
            return_document=ReturnDocument.AFTER,
        )
    
    async def delete(self, id: str ) -> Candidate | None:
        deleted_candidate = self.db.candidate.find_one(
            {"_id": ObjectId(id)}
        ) 
        self.db.candidate.delete_one({"_id": ObjectId(id)})
        return deleted_candidate