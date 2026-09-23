import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.core import WeeklyTask
from app.models.enums import TaskStatus
from app.repositories import task_repo
from app.schemas import WeeklyTaskCreate, WeeklyTaskUpdate


async def create_task(db: AsyncSession, payload: WeeklyTaskCreate) -> WeeklyTask:
    task = WeeklyTask(
        id=uuid.uuid4(),
        game_plan_id=payload.game_plan_id,
        role_id=payload.role_id,
        assigned_staff_member_id=payload.assigned_staff_member_id,
        title=payload.title,
        description=payload.description,
        cycle_day=payload.cycle_day,
        cycle_phase=payload.cycle_phase,
        status=TaskStatus.not_started,
        due_at=payload.due_at,
    )
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def update_task(db: AsyncSession, task_id: uuid.UUID, payload: WeeklyTaskUpdate) -> WeeklyTask | None:
    task = await task_repo.get_task(db, task_id)
    if task is None:
        return None
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(task, field, value)
    await db.commit()
    await db.refresh(task)
    return task


async def apply_template(
    db: AsyncSession, source_game_plan_id: uuid.UUID, target_game_plan_id: uuid.UUID
) -> list[WeeklyTask]:
    """Copy a prior week's task structure onto a new GamePlan (status reset to not_started)."""
    source_tasks = await task_repo.list_tasks(db, source_game_plan_id)
    new_tasks = [
        WeeklyTask(
            id=uuid.uuid4(),
            game_plan_id=target_game_plan_id,
            role_id=t.role_id,
            assigned_staff_member_id=t.assigned_staff_member_id,
            title=t.title,
            description=t.description,
            cycle_day=t.cycle_day,
            cycle_phase=t.cycle_phase,
            status=TaskStatus.not_started,
            due_at=None,
        )
        for t in source_tasks
    ]
    db.add_all(new_tasks)
    await db.commit()
    for t in new_tasks:
        await db.refresh(t)
    return new_tasks

