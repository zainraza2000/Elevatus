from fastapi import APIRouter

from .router import candidate_router

sub_router = APIRouter()
sub_router.include_router(candidate_router, prefix="", tags=["Candidate"])


__all__ = ["sub_router"]