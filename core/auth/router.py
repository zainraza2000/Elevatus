from fastapi import APIRouter
from core.auth.dtos.request import AuthRequest
from core.auth.dtos.response import AuthResponse 
from core.auth.service import AuthService

auth_router = APIRouter()


@auth_router.post("/token",response_model=AuthResponse)
async def get_token(payload: AuthRequest):
    return await AuthService().get_token(payload=payload)