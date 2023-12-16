from fastapi import APIRouter, Query, Depends,status
from core._models.candidate import Candidate
from core.candidate.service import CandidateService
from core.candidate.dtos.request import CandidateUpdate
from typing import List,Annotated
from core._models.user import User
from core._utils.auth_helper import verify_token

candidate_router = APIRouter(tags=["Candidate"])

@candidate_router.get("/all-candidates",response_model=List[Candidate])
async def get_candidates_by_keyword(current_user: Annotated[User, Depends(verify_token)],keyword: str = Query(None, title="Search Keyword", description="Global search keyword")):
    return await CandidateService().get_candidates_by_keyword(keyword)

@candidate_router.get("/candidate/{candidate_id}",response_model=Candidate)
async def get_candidate_by_id(current_user: Annotated[User, Depends(verify_token)],candidate_id: str | int):
    return await CandidateService().get_candidate(candidate_id=candidate_id)

@candidate_router.post("/candidate",response_model=Candidate,status_code=status.HTTP_201_CREATED)
async def create_candidate(current_user: Annotated[User, Depends(verify_token)],candidate: Candidate):
    return await CandidateService().create_candidate(candidate=candidate)

@candidate_router.put("/candidate/{candidate_id}",response_model=Candidate)
async def update_candidate(current_user: Annotated[User, Depends(verify_token)],candidate_id: str | int, candidate: CandidateUpdate):
    return await CandidateService().update_candidate(candidate=candidate,candidate_id=candidate_id)

@candidate_router.delete("/candidate/{candidate_id}",response_model=Candidate)
async def delete_candidate(current_user: Annotated[User, Depends(verify_token)], candidate_id: str | int):
    return await CandidateService().delete_candidate(candidate_id=candidate_id)

@candidate_router.get("/generate-report")
async def generate_report():
    return await CandidateService().generate_report()
