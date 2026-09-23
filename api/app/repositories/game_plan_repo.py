import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.core import GamePlan


async def get_game_plan(db: AsyncSession, game_plan_id: uuid.UUID) -> GamePlan | None:
    return await db.get(GamePlan, game_plan_id)


async def list_game_plans(db: AsyncSession, team_id: uuid.UUID | None = None) -> list[GamePlan]:
    stmt = select(GamePlan)
    if team_id is not None:
        stmt = stmt.where(GamePlan.team_id == team_id)
    result = await db.execute(stmt.order_by(GamePlan.game_date.desc()))
    return list(result.scalars().all())
