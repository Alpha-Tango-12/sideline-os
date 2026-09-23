import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.core import WeeklyTask
from app.models.enums import CycleDay


async def list_tasks(
    db: AsyncSession,
    game_plan_id: uuid.UUID,
    role_id: uuid.UUID | None = None,
    cycle_day: CycleDay | None = None,
) -> list[WeeklyTask]:
    stmt = select(WeeklyTask).where(WeeklyTask.game_plan_id == game_plan_id)
    if role_id is not None:
        stmt = stmt.where(WeeklyTask.role_id == role_id)
    if cycle_day is not None:
        stmt = stmt.where(WeeklyTask.cycle_day == cycle_day)
    result = await db.execute(stmt)
    return list(result.scalars().all())


async def get_task(db: AsyncSession, task_id: uuid.UUID) -> WeeklyTask | None:
    return await db.get(WeeklyTask, task_id)
