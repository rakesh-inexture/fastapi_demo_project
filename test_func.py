# Test your FastAPI endpoints

# GET http://127.0.0.1:8000/
# Accept: application/json

###

# GET http://127.0.0.1:8000/hello/User
# Accept: application/json

###

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "HELLO WORLD"}
