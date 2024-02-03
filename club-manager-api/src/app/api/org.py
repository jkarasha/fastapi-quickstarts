from fastapi import APIRouter, status
from app.api import crud
from app.api.models import OrgSchema, OrgDB

org_router = APIRouter()

@org_router.post("/create", response_model=OrgDB, status_code=status.HTTP_201_CREATED)
async def create_org(payload: OrgSchema):
    org_id = await crud.post(payload)

    response_object = {
        "id": org_id,
        "name": payload.name,
        "description": payload.description,
        "street": payload.street,
        "city": payload.city,
        "state": payload.state,
        "zip": payload.zip
    }

    return response_object