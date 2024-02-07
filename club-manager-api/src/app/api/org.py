from fastapi import APIRouter, HTTPException, status
from app.api.crud import orgs as crud
from app.api.models.orgs import OrgSchema, OrgDB

org_router = APIRouter()

@org_router.post("/", response_model=OrgDB, status_code=status.HTTP_201_CREATED)
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

@org_router.get("/{id}", response_model=OrgDB)
async def read_org(id: int):
    org = await crud.get(id)
    if not org:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Org with given id not found")
    return org

@org_router.get("/", response_model=list[OrgDB])
async def read_all_orgs():
    return await crud.get_all()

@org_router.put("/{id}", response_model=OrgDB)
async def update_org(id: int, payload: OrgSchema):
    org = await crud.get(id)
    if not org:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Org with given id not found")
    org_id = await crud.put(id, payload)

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

@org_router.delete("/{id}", response_model=OrgDB)
async def delete_org(id: int):
    org = await crud.get(id)
    if not org:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Org with given id not found")
    await crud.delete(id)
    return org