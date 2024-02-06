import json
from fastapi import status
from app.api.crud import users as crud

def test_create_user(test_app, monkeypatch):
    test_request_payload = {"username": "testuser", "email": "user@example.com", "password": "password"}
    test_response_payload = {"id": 1, "username": "testuser", "email": "testuser@example.com"}

    async def mock_post(payload):
        return 1
    monkeypatch.setattr(crud, "post", mock_post)
    response = test_app.post("/users/", data=json.dumps(test_request_payload))
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == test_response_payload
    
