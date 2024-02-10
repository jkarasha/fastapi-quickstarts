import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, status, Depends

from app.db import models
from app.db.session import get_db_session

org_router = APIRouter()

@org_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_org(
    data: models.Organization,
    session: AsyncSession = Depends(get_db_session),
    ) -> models.Organization:
    org = models.Organization(**data.model_dump())
    session.add(org)
    await session.commit()
    await session.refresh(org)
    return models.Organization.model_validate(org)

@org_router.get("/{id}")
async def get_org(
    pk: uuid.UUID,
    session: AsyncSession = Depends(get_db_session),
    ) -> models.Organization:
    org = await session.get(models.Organization, pk)
    if org is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Org with given id not found")
    
    return models.Organization.model_validate(org)

@org_router.get("/")
async def get_all_orgs(
    session: AsyncSession = Depends(get_db_session),
) -> list[models.Organization]:
    orgs = await session.scalars(select(models.Organization))