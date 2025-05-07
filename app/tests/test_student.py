from fastapi.testclient import TestClient
from app.main import app  # import your FastAPI app

client = TestClient(app)

def test_get_students():
    response = client.get("/students")
    assert response.status_code == 200
    assert "data" in response.json()
