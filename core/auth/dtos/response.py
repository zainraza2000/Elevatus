from pydantic import BaseModel

class AuthResponse(BaseModel):
    api_key: str