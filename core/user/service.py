from pythondi import inject
from core._repositories.abstract.user import UserRepository
from core._models.user import User
from fastapi import HTTPException,status
class UserService:
    @inject()
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    async def create_user(self, user: User):
        #if user with email already exists
        is_exist = await self.user_repository.find_one({"email": user.email})
        if is_exist:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email already exists")
        return await self.user_repository.create(user)
    
    async def get_user_by_id(self, user_id: str):
        return await self.user_repository.get_by_id(user_id)