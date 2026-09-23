import uuid

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.playbook import Formation, PersonnelGroup, Play

router = APIRouter(tags=["playbook"])


@router.get("/personnel-groups")
async def list_personnel_groups(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PersonnelGroup))
    return result.scalars().all()


@router.get("/formations")
async def list_formations(personnel_group_id: uuid.UUID | None = None, db: AsyncSession = Depends(get_db)):
    stmt = select(Formation)
    if personnel_group_id is not None:
        stmt = stmt.where(Formation.personnel_group_id == personnel_group_id)
    result = await db.execute(stmt)
    return result.scalars().all()


@router.get("/plays")
async def list_plays(formation_id: uuid.UUID | None = None, db: AsyncSession = Depends(get_db)):
    stmt = select(Play)
    if formation_id is not None:
        stmt = stmt.where(Play.formation_id == formation_id)
    result = await db.execute(stmt)
    return result.scalars().all()
