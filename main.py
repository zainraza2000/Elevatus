from fastapi import FastAPI
from core import router
from fastapi.testclient import TestClient

#entrypoint

app = FastAPI(
    title="Docs",
    summary="A sample application created for test assignment for Elevatus",
)

app.include_router(router)
