from fastapi import APIRouter
from core._models.user import User
from core.user.service import UserService

health_router = APIRouter()

@health_router.get("/health")
async def health_check():
    return "Success"