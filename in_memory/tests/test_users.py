from fastapi.testclient import TestClient

from app.main import app
from app.services.user_service import repository

client = TestClient(app)
USER_PAYLOAD = {
    "name": "John Doe",
    "email": "john@example.com",
    "password": "password123",
}


def setup_function():
    repository.users.clear()
    repository.next_id = 1


def test_create_user():
    response = client.post("/users/", json=USER_PAYLOAD)

    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"


def test_get_users():
    client.post("/users/", json=USER_PAYLOAD)

    response = client.get("/users/")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_duplicate_email():
    client.post("/users/", json=USER_PAYLOAD)
    response = client.post("/users/", json=USER_PAYLOAD)

    assert response.status_code == 400


def test_delete_user():
    response = client.post("/users/", json=USER_PAYLOAD)

    user_id = response.json()["id"]

    delete_response = client.delete(f"/users/{user_id}")

    assert delete_response.status_code == 204