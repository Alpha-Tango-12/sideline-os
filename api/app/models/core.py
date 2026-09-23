import uuid
from datetime import date, datetime

from sqlalchemy import Date, DateTime, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.models.base import TimestampMixin, UUIDPKMixin
from app.models.enums import CycleDay, CyclePhase, GamePlanStatus, PermissionScope, TaskStatus


class Team(Base, UUIDPKMixin):
    __tablename__ = "teams"

    name: Mapped[str] = mapped_column(String(255))


class StaffMember(Base, UUIDPKMixin):
    __tablename__ = "staff_members"

    team_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("teams.id"))
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(320), unique=True, index=True)


class Role(Base, UUIDPKMixin):
    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    permission_scope: Mapped[PermissionScope] = mapped_column(Enum(PermissionScope))


class RoleAssignment(Base, UUIDPKMixin):
    __tablename__ = "role_assignments"

    game_plan_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("game_plans.id"))
    staff_member_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("staff_members.id"))
    role_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("roles.id"))


class GamePlan(Base, UUIDPKMixin, TimestampMixin):
    __tablename__ = "game_plans"

    team_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("teams.id"))
    opponent_name: Mapped[str] = mapped_column(String(255))
    season: Mapped[int]
    week_number: Mapped[int]
    game_date: Mapped[date] = mapped_column(Date)
    status: Mapped[GamePlanStatus] = mapped_column(Enum(GamePlanStatus), default=GamePlanStatus.planning)


class WeeklyTask(Base, UUIDPKMixin, TimestampMixin):
    __tablename__ = "weekly_tasks"

    game_plan_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("game_plans.id"))
    role_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("roles.id"))
    assigned_staff_member_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("staff_members.id"), nullable=True
    )
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String(2000), nullable=True)
    cycle_day: Mapped[CycleDay] = mapped_column(Enum(CycleDay))
    cycle_phase: Mapped[CyclePhase] = mapped_column(Enum(CyclePhase))
    status: Mapped[TaskStatus] = mapped_column(Enum(TaskStatus), default=TaskStatus.not_started)
    due_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    linked_entity_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    linked_entity_id: Mapped[uuid.UUID | None] = mapped_column(nullable=True)
