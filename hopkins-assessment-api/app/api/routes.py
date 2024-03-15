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