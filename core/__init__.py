from pythondi import Provider, configure
from core._repositories.abstract.user import UserRepository
from core._repositories.abstract.candidate import CandidateRepository
from core._repositories.mongo.user import UserMongoRepository
from core._repositories.mongo.candidate import CandidateMongoRepository

from fastapi import APIRouter

from core.user import sub_router as user_router
from core.health import health_router
from core.candidate import sub_router as candidate_router
from core.auth import sub_router as auth_router

#including all routers in the module

router = APIRouter()
router.include_router(auth_router)
router.include_router(user_router)
router.include_router(candidate_router)
router.include_router(health_router)



__all__ = ["router"]

def init_dependency_injection():
    provider = Provider()
    provider.bind(UserRepository, UserMongoRepository)
    provider.bind(CandidateRepository, CandidateMongoRepository)
    configure(provider=provider)



init_dependency_injection()