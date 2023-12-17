from main import app
from fastapi.testclient import TestClient

client = TestClient(app=app)

payload = {
  "first_name": "string",
  "last_name": "string",
  "email": "user@example.com",
  "career_level": "string",
  "job_major": "string",
  "years_of_experience": 0,
  "degree_type": "string",
  "skills": [
    "string"
  ],
  "nationality": "string",
  "city": "string",
  "salary": 0,
  "gender": "Male"
}
keyword = "zain"

def get_api_key(email: str):
    response = client.post(
        "/token",
        json={"email": email},
    )
    assert response.status_code == 200
    return response.json()["api_key"]

def test_candidate_crud(pytestconfig):
    api_key = get_api_key(pytestconfig.getoption('email'))
    response = client.post(
        "/candidate",
        headers={"Api_key": api_key},
        json=payload
    )
    doc = response.json()
    assert response.status_code == 201
    assert doc["first_name"] == "string"
    created_id = doc["_id"]
    response = client.get(f"/candidate/{created_id}",headers={"Api_key": api_key})
    doc = response.json()
    assert response.status_code == 200
    assert doc["first_name"] == "string"
    response = client.put(
        f"/candidate/{created_id}",
        headers={"Api_key": api_key},
        json={"first_name": "zain"}
    )
    doc = response.json()
    assert doc["first_name"] == "zain"
    assert response.status_code == 200
    response = client.get(
        f"/all-candidates?keyword={keyword}",
        headers={"Api_key": api_key},
    )
    doc = response.json()
    assert doc[0]["first_name"] == "zain"
    assert response.status_code == 200
    response = client.get(
        f"/all-candidates?keyword={keyword}",
        headers={"Api_key": api_key},
    )
    doc = response.json()
    assert doc[0]["first_name"] == "zain"
    assert response.status_code == 200
    response = client.get(
        "/generate-report"
    )
    assert "Generated" in response.text
    assert response.status_code == 200
    response = client.delete(
        f"candidate/{created_id}",
        headers={"Api_key": api_key},
    )
    doc = response.json()
    assert response.status_code == 200
    assert doc["first_name"] == "zain"