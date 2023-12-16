from fastapi import APIRouter

from .router import user_router

sub_router = APIRouter()
sub_router.include_router(user_router, prefix="/user", tags=["User"])


__all__ = ["sub_router"]