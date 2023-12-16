from fastapi import APIRouter
from core._models.user import User
from core.user.service import UserService

user_router = APIRouter()

@user_router.post("",response_model=User,response_model_exclude={"uuid"})
async def create_user(user: User):
    return await UserService().create_user(user)
