import uuid
from datetime import date

from sqlalchemy import Date, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.models.base import UUIDPKMixin
from app.models.enums import DownDistanceBucket, ScoutCardGenerationMode, ScriptStatus, Tempo


class PracticeScript(Base, UUIDPKMixin):
    __tablename__ = "practice_scripts"

    game_plan_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("game_plans.id"))
    practice_date: Mapped[date] = mapped_column(Date)
    generated_from_sideline_sheet_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("sideline_sheets.id"), nullable=True
    )
    status: Mapped[ScriptStatus] = mapped_column(Enum(ScriptStatus), default=ScriptStatus.draft)


class ScriptPeriod(Base, UUIDPKMixin):
    __tablename__ = "script_periods"

    practice_script_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("practice_scripts.id"))
    period_number: Mapped[int]
    period_name: Mapped[str] = mapped_column(String(100))
    tempo: Mapped[Tempo] = mapped_column(Enum(Tempo))
    duration_minutes: Mapped[int | None] = mapped_column(nullable=True)


class ScriptRep(Base, UUIDPKMixin):
    __tablename__ = "script_reps"

    script_period_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("script_periods.id"))
    play_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("plays.id"))
    personnel_group_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("personnel_groups.id"))
    rep_order: Mapped[int]
    down_distance_bucket: Mapped[DownDistanceBucket] = mapped_column(Enum(DownDistanceBucket))
    notes: Mapped[str | None] = mapped_column(String(1000), nullable=True)


class ScoutCard(Base, UUIDPKMixin):
    __tablename__ = "scout_cards"

    game_plan_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("game_plans.id"))
    title: Mapped[str] = mapped_column(String(255))
    generation_mode: Mapped[ScoutCardGenerationMode] = mapped_column(
        Enum(ScoutCardGenerationMode), default=ScoutCardGenerationMode.manual_assist
    )


class ScoutCardEntry(Base, UUIDPKMixin):
    __tablename__ = "scout_card_entries"

    scout_card_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("scout_cards.id"))
    opponent_play_label: Mapped[str] = mapped_column(String(255))
    formation_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("formations.id"), nullable=True)
    down_distance_bucket: Mapped[DownDistanceBucket] = mapped_column(Enum(DownDistanceBucket))
    frequency_note: Mapped[str | None] = mapped_column(String(500), nullable=True)
    source_clip_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("video_clips.id"), nullable=True)
    sort_order: Mapped[int]
