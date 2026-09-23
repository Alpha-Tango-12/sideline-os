import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.enums import CycleDay
from app.repositories import task_repo
from app.schemas import WeeklyTaskCreate, WeeklyTaskRead, WeeklyTaskUpdate
from app.services import workflow_service

router = APIRouter(tags=["tasks"])


@router.get("/gameplans/{game_plan_id}/tasks", response_model=list[WeeklyTaskRead])
async def list_tasks(
    game_plan_id: uuid.UUID,
    role: uuid.UUID | None = None,
    day: CycleDay | None = None,
    db: AsyncSession = Depends(get_db),
):
    return await task_repo.list_tasks(db, game_plan_id, role_id=role, cycle_day=day)


@router.post("/tasks", response_model=WeeklyTaskRead, status_code=201)
async def create_task(payload: WeeklyTaskCreate, db: AsyncSession = Depends(get_db)):
    return await workflow_service.create_task(db, payload)


@router.patch("/tasks/{task_id}", response_model=WeeklyTaskRead)
async def update_task(task_id: uuid.UUID, payload: WeeklyTaskUpdate, db: AsyncSession = Depends(get_db)):
    task = await workflow_service.update_task(db, task_id, payload)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("/gameplans/{game_plan_id}/tasks/apply-template", response_model=list[WeeklyTaskRead])
async def apply_template(
    game_plan_id: uuid.UUID,
    source_game_plan_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
):
    return await workflow_service.apply_template(db, source_game_plan_id, game_plan_id)
