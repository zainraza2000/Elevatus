from main import app
from fastapi.testclient import TestClient
import pytest

client = TestClient(app=app)

payload = {
  "email": "jdoe@example.com",
  "first_name": "Zain",
  "last_name": "Raza"
}

def test_user():
    response = client.post('/user',json=payload)
    assert response.status_code == 200
