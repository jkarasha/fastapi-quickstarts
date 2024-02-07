import json
from fastapi import status

import app.api.crud.orgs as crud

def test_create_org(test_app, monkeypatch):
    test_request_payload = {"name": "Nokea", "description": "Northwest Kenyans Association", "street": "1234 NW 5th Ave, Portland, OR 97209", "city": "Portland", "state": "OR", "zip": "97209"}
    test_response_payload = {"id": 1, "name": "Nokea", "description": "Northwest Kenyans Association", "street": "1234 NW 5th Ave, Portland, OR 97209", "city": "Portland", "state": "OR", "zip": "97209"}

    async def mock_post(payload):
        return 1
    #
    monkeypatch.setattr(crud, "post", mock_post)
    response = test_app.post("/orgs/", data=json.dumps(test_request_payload))
    #
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == test_response_payload

def test_read_org(test_app, monkeypatch):
    test_data = {"id": 1, "name": "Nokea", "description": "Northwest Kenyans Association", "street": "1234 NW 5th Ave, Portland, OR 97209", "city": "Portland", "state": "OR", "zip": "97209"}
    async def mock_get(id):
        return test_data
    monkeypatch.setattr(crud, "get", mock_get)
    response = test_app.get("/orgs/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == test_data

def test_read_org_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None
    monkeypatch.setattr(crud, "get", mock_get)
    response = test_app.get("/orgs/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "Org with given id not found"

def test_read_all_orgs(test_app, monkeypatch):
    test_data = [
        {"id": 1, "name": "Nokea", "description": "Northwest Kenyans Association", "street": "1234 NW 5th Ave", "city": "Portland", "state": "OR", "zip": "97209"},
        {"id": 2, "name": "Nokea Investment", "description": "Northwest Kenyans Investment Club", "street": "1234 NW 5th Ave", "city": "Portland", "state": "OR", "zip": "97209"},
        ]
    
    async def mock_get_all():
        return test_data
    monkeypatch.setattr(crud, "get_all", mock_get_all)

    response = test_app.get("/orgs/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == test_data

def test_update_org(test_app, monkeypatch):
    test_update_data = {"id": 1, "name": "Nokea", "description": "Northwest Kenyans Association", "street": "102 Main St.", "city": "Spokane", "state": "WA", "zip": "99206"}
    
    async def mock_get(id):
        return True
    monkeypatch.setattr(crud, "get", mock_get)

    async def mock_put(id, payload):
        return 1
    monkeypatch.setattr(crud, "put", mock_put)

    response = test_app.put("/orgs/1", data=json.dumps(test_update_data)) 
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == test_update_data

def test_delete_org(test_app, monkeypatch):
    test_data = {"id": 1, "name": "Nokea", "description": "Northwest Kenyans Association", "street": "1234 NW 5th Ave", "city": "Portland", "state": "OR", "zip": "97209"}
    async def mock_get(id):
        return test_data
    monkeypatch.setattr(crud, "get", mock_get)

    async def mock_delete(id):
        return id
    monkeypatch.setattr(crud, "delete", mock_delete)

    response = test_app.delete("/orgs/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == test_data
