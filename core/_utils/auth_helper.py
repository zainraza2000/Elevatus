from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from jose import JWTError, jwt
from settings import settings
from core.user.service import UserService

access_token = APIKeyHeader(name="api_key")

#simple api key auth token consists of email and id
async def verify_token(token: str = Depends(access_token)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid api key",
            headers={"WWW-Authenticate": "Key"},
        )
        try:
            payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
            # if user with id in the token exists
            user = await UserService().get_user_by_id(payload["sub"])
            if user:
                return payload
            else:
                raise JWTError
        except JWTError:
            raise credentials_exception