from pythondi import inject
from core._repositories.abstract.candidate import CandidateRepository
from core._models.candidate import Candidate
from core.candidate.dtos.request import CandidateUpdate
from datetime import datetime
import pandas as pd
import os
from fastapi import HTTPException,status

class CandidateService:
    @inject()
    def __init__(self, candidate_repository: CandidateRepository):
        self.candidate_repository = candidate_repository
    
    async def create_candidate(self, candidate: Candidate):
        return await self.candidate_repository.create(candidate)
    
    async def get_candidate(self, candidate_id: str | int):
        return await self.candidate_repository.get_by_id(candidate_id)

    async def update_candidate(self, candidate_id: str | int, candidate: CandidateUpdate):
        return await self.candidate_repository.update(candidate_id,candidate)
    
    async def delete_candidate(self, candidate_id: str | int):
        return await self.candidate_repository.delete(candidate_id)
    
    async def get_candidates_by_keyword(self,keyword):
        # global keyword search
        query = {}
        if keyword:
            search_keys = [field for field in Candidate.__annotations__.keys() if field != 'uuid']
            query["$or"] = [
                {field: {"$regex": f".*{keyword}.*", "$options": "i"}}
                for field in search_keys
            ]
        return await self.candidate_repository.find(query)
    
    async def generate_report(self):
        #generating report containing data for all candidates
        file_name = f'report_{datetime.now().timestamp()}'
        candidates = await self.candidate_repository.get_all()
        list_of_candidates = [model.model_dump() for model in candidates]
        if len(list_of_candidates) == 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No candidates exist")
        df = pd.DataFrame(list_of_candidates)
        reports_folder = "reports"
        if not os.path.exists(reports_folder):
            os.makedirs(reports_folder)
        csv_file_path = os.path.join(reports_folder, f'{file_name}.csv')
        df.to_csv(csv_file_path, index=False)
        return f"Generated report in {csv_file_path}"