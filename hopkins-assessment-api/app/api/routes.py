from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import schemas
from app.database import models as db_models
from app.database.session import get_db_session

router = APIRouter(prefix="/v1", tags=["v1"])

@router.post("/assessor", status_code=status.HTTP_201_CREATED)
async def create_assessor(
    data: schemas.AssessorPayload,
    session: AsyncSession = Depends(get_db_session)
) -> schemas.Assessor:
    assessor = db_models.Assessor(**data.model_dump())
    session.add(assessor)
    await session.commit()
    await session.refresh(assessor)
    return schemas.Assessor.model_validate(assessor)

@router.get("/assessor", status_code=status.HTTP_200_OK)
async def get_assessors(
    session: AsyncSession = Depends(get_db_session)
) -> list[schemas.Assessor]:
    assessors = await session.scalars(select(db_models.Assessor))
    return [schemas.Assessor.model_validate(assessor) for assessor in assessors]

@router.get("/assessor/{pk}", status_code=status.HTTP_200_OK)
async def get_assessor(
    pk: int,
    session: AsyncSession = Depends(get_db_session)
) -> schemas.Assessor:
    assessor = await session.get(db_models.Assessor, pk)
    if assessor is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Assessor does not exist"
        )
    return schemas.Assessor.model_validate(assessor)

@router.post("/role", status_code=status.HTTP_201_CREATED)
async def create_role(
    data: schemas.RolePayload,
    session: AsyncSession = Depends(get_db_session)
) -> schemas.Role:
    role = db_models.Role(**data.model_dump())
    session.add(role)
    await session.commit()
    await session.refresh(role)
    return schemas.Role.model_validate(role)

@router.get("/role", status_code=status.HTTP_200_OK)
async def get_roles(
    session: AsyncSession = Depends(get_db_session)
) -> list[schemas.Role]:
    roles = await session.scalars(select(db_models.Role))
    return [schemas.Role.model_validate(role) for role in roles]

@router.get("/role/{pk}", status_code=status.HTTP_200_OK)
async def get_role(
    pk: int,
    session: AsyncSession = Depends(get_db_session)
) -> schemas.Role:
    role = await session.get(db_models.Role, pk)
    if role is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role does not exist"
        )
    return schemas.Role.model_validate(role)