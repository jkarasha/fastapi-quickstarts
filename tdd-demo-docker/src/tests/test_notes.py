import json
import pytest
from fastapi import status

from app.api import crud

def test_create_note(test_app, monkeypatch):
    test_request_payload = {"title": "something", "description": "something else"}
    test_response_payload = {"id":1, "title": "something", "description": "something else"}

    async def mock_post(payload):
        return 1
    #
    monkeypatch.setattr(crud, "post", mock_post)
    response = test_app.post("/notes/", data=json.dumps(test_request_payload),)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == test_response_payload

def test_create_note_invalid_json(test_app):
    response = test_app.post("/notes/", content=json.dumps({"title": "something"}))
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_read_note(test_app, monkeypatch):
    test_data = {"id": 1, "title": "something", "description": "something else"}

    async def mock_get(id):
        return test_data
    
    monkeypatch.setattr(crud, "get", mock_get)
    response = test_app.get("/notes/1")
    #
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == test_data

def test_read_note_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None
    #
    monkeypatch.setattr(crud, "get", mock_get)
    #
    response = test_app.get("/notes/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "Note not found"
    #
    response = test_app.get("/notes/0")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_read_all_notes(test_app, monkeypatch):
    test_data = [
        {"id": 1, "title": "something", "description": "something else"},
        {"id": 2, "title": "someone", "description": "someone else"}
    ]
    #
    async def mock_get_all():
        return test_data
    #
    monkeypatch.setattr(crud, "get_all", mock_get_all)
    #
    response = test_app.get("/notes/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == test_data

def test_update_note(test_app, monkeypatch):
    test_update_data = {"id": 1, "title": "someone", "description": "someone else"}

    async def mock_get(id):
        return True
    monkeypatch.setattr(crud, "get", mock_get)
    #
    async def mock_put(id, payload):
        return 1
    monkeypatch.setattr(crud, "put", mock_put)
    #
    response = test_app.put("/notes/1/", data=json.dumps(test_update_data))
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == test_update_data
    #

@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1, {"title": "bar"}, 422],
        [999, {"title": "foo", "description": "bar"}, 404],
    ]

)

def test_update_note_invalid(test_app, monkeypatch, id, payload, status_code):
    async def mock_get(id):
        return None
    #
    monkeypatch.setattr(crud, "get", mock_get)
    #
    response = test_app.put(f"/notes/{id}/", data=json.dumps(payload),)
    assert response.status_code == status_code

def test_remove_note(test_app, monkeypatch):
    test_data = {"title": "something", "description": "something else", "id": 1}

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    async def mock_delete(id):
        return id

    monkeypatch.setattr(crud, "delete", mock_delete)

    response = test_app.delete("/notes/1/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == test_data

def test_remove_note_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.delete("/notes/999/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "Note not found"