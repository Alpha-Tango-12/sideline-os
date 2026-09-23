import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.enums import CycleDay
from app.repositories import game_plan_repo, task_repo
from app.schemas import GamePlanRead

router = APIRouter(prefix="/gameplans", tags=["game-plans"])


@router.get("/{game_plan_id}", response_model=GamePlanRead)
async def get_game_plan(game_plan_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    game_plan = await game_plan_repo.get_game_plan(db, game_plan_id)
    if game_plan is None:
        raise HTTPException(status_code=404, detail="GamePlan not found")
    return game_plan


@router.get("/{game_plan_id}/weekly-cycle")
async def get_weekly_cycle(game_plan_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    game_plan = await game_plan_repo.get_game_plan(db, game_plan_id)
    if game_plan is None:
        raise HTTPException(status_code=404, detail="GamePlan not found")

    tasks = await task_repo.list_tasks(db, game_plan_id)
    days = {}
    for day in CycleDay:
        day_tasks = [t for t in tasks if t.cycle_day == day]
        done = sum(1 for t in day_tasks if t.status == "done")
        days[day.value] = {
            "cycle_phase": day_tasks[0].cycle_phase.value if day_tasks else None,
            "tasks_total": len(day_tasks),
            "tasks_done": done,
        }
    return {"game_plan_id": str(game_plan_id), "days": days}
