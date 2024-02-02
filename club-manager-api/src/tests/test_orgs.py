import json
from fastapi import status

from app.api import crud

def test_create_org(test_app, monkeypatch):
    test_request_payload = {"title": "Nokea", "description": "Northwest Kenyans Association"}
    test_response_payload = {"id": 1, "title": "Nokea", "description": "Northwest Kenyans Association"}

    async def mock_post(payload):
        return 1
    #
    monkeypatch.setattr(crud, "post", mock_post)
    response = test_app.post("/org/", data=json.dumps(test_request_payload))
    #
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == test_response_payload

