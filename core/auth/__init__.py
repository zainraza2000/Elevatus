from fastapi import APIRouter

from .router import auth_router

sub_router = APIRouter()
sub_router.include_router(auth_router, prefix="", tags=["Auth"])


__all__ = ["sub_router"]