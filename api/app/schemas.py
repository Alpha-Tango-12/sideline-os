import uuid
from datetime import date, datetime

from pydantic import BaseModel, ConfigDict

from app.models.enums import CycleDay, CyclePhase, GamePlanStatus, TaskStatus


class GamePlanRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    opponent_name: str
    season: int
    week_number: int
    game_date: date
    status: GamePlanStatus


class WeeklyTaskRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    game_plan_id: uuid.UUID
    role_id: uuid.UUID
    assigned_staff_member_id: uuid.UUID | None
    title: str
    description: str | None
    cycle_day: CycleDay
    cycle_phase: CyclePhase
    status: TaskStatus
    due_at: datetime | None
    linked_entity_type: str | None
    linked_entity_id: uuid.UUID | None


class WeeklyTaskCreate(BaseModel):
    game_plan_id: uuid.UUID
    role_id: uuid.UUID
    assigned_staff_member_id: uuid.UUID | None = None
    title: str
    description: str | None = None
    cycle_day: CycleDay
    cycle_phase: CyclePhase
    due_at: datetime | None = None


class WeeklyTaskUpdate(BaseModel):
    status: TaskStatus | None = None
    assigned_staff_member_id: uuid.UUID | None = None
    title: str | None = None
    description: str | None = None


class RoleRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    description: str | None
    permission_scope: str
