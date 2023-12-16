from fastapi import FastAPI
from core.user.router import user_router
from core.candidate.router import candidate_router
from core import router
from fastapi.testclient import TestClient
import pytest

app = FastAPI(
    title="Elevatus Assignment",
    summary="A sample application created for test assignment for Elevatus",
)

app.include_router(router)
