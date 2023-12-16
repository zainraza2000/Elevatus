from pythondi import inject
from core._repositories.abstract.user import UserRepository
from core.auth.dtos.request import AuthRequest
from core.auth.dtos.response import AuthResponse
from fastapi import HTTPException
from jose import jwt
from settings import settings
from core._models.user import User
@inject()
class AuthService:
    @inject()
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    async def create_access_token(self, data: dict):
        to_encode = data.copy()
        encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
        return encoded_jwt

    async def get_token(self, payload: AuthRequest):
        try:
            user = User.model_validate(await self.user_repository.get_by_email(payload.email))
            api_key = await self.create_access_token(
                data={"sub": str(user.uuid), "email": payload.email}
            )
            return AuthResponse(api_key=api_key)
        except:
            raise HTTPException(status_code=401, detail="Invalid credentials")


    