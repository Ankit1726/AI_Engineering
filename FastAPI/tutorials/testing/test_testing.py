from fastapi.testclient import TestClient
from tutorials.src.testing.testing import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello AI Dev Ankit"}


def test_add_nums():
    response = client.get("/add?a=5&b=3")

    assert response.status_code == 200
    assert response.json() == {"result": 8}