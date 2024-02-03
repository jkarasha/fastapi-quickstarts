import json
from fastapi import status

from app.api import crud

def test_create_org(test_app, monkeypatch):
    test_request_payload = {"name": "Nokea", "description": "Northwest Kenyans Association", "street": "1234 NW 5th Ave, Portland, OR 97209", "city": "Portland", "state": "OR", "zip": "97209"}
    test_response_payload = {"id": 1, "name": "Nokea", "description": "Northwest Kenyans Association", "street": "1234 NW 5th Ave, Portland, OR 97209", "city": "Portland", "state": "OR", "zip": "97209"}

    async def mock_post(payload):
        return 1
    #
    monkeypatch.setattr(crud, "post", mock_post)
    response = test_app.post("/org/create", data=json.dumps(test_request_payload))
    #
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == test_response_payload

