import json
from fastapi import status
from app.api.crud import users as crud

def test_create_user(test_app, monkeypatch):
    test_request_payload = {"username": "testuser", "email": "testuser@example.com", "password": "password"}
    test_response_payload = {"id": 1, "username": "testuser", "email": "testuser@example.com", "password": "password"}

    async def mock_post(payload):
        return 1
    monkeypatch.setattr(crud, "post", mock_post)
    response = test_app.post("/users/", data=json.dumps(test_request_payload))
    #
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == test_response_payload

def test_read_user(test_app, monkeypatch):
    test_data = {"id": 1, "username": "testuser", "email": "testuser@example.com", "password": "password"}
    async def mock_get(id):
        return test_data
    monkeypatch.setattr(crud, "get", mock_get)
    response = test_app.get("/users/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == test_data

def test_read_user_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None
    monkeypatch.setattr(crud, "get", mock_get)
    response = test_app.get("/users/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "User with given id not found"  

def test_read_all_users(test_app, monkeypatch):
    test_data = [
        {"id": 1, "username": "testuser", "email": "testuser@example.com", "password": "password"},
        {"id": 2, "username": "testuser2", "email": "testuser2@examplecom", "password": "password2"},
    ]
    async def mock_get_all():
        return test_data
    monkeypatch.setattr(crud, "get_all", mock_get_all)
    response = test_app.get("/users/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == test_data

def test_update_user(test_app, monkeypatch):
    test_update_data = {"id": 1, "username": "testuser", "email": "testuser@example.com", "password": "password"}
    async def mock_get(id):
        return True
    monkeypatch.setattr(crud, "get", mock_get)
    async def mock_put(id, payload):
        return 1
    monkeypatch.setattr(crud, "put", mock_put)
    response = test_app.put("/users/1", data=json.dumps(test_update_data))
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == test_update_data

def test_update_user_incorrect_id(test_app, monkeypatch):
    test_update_data = {"id": 1, "username": "testuser", "email": "testuser@example.com", "password": "password"}
    async def mock_get(id):
        return None
    monkeypatch.setattr(crud, "get", mock_get)
    response = test_app.put("/users/999", data=json.dumps(test_update_data))
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "User with given id not found"

def test_delete_user(test_app, monkeypatch):
    test_data = {"id": 1, "username": "testuser", "email": "testuser@example.com", "password": "password"}
    async def mock_get(id):
        return test_data
    monkeypatch.setattr(crud, "get", mock_get)
    async def mock_delete(id):
        return id
    monkeypatch.setattr(crud, "delete", mock_delete)
    response = test_app.delete("/users/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == test_data
    

