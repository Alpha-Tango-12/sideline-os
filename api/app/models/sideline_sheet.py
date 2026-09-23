import uuid

from sqlalchemy import Boolean, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.models.base import TimestampMixin, UUIDPKMixin
from app.models.enums import DownDistanceBucket, FieldZone, HashPosition


class SidelineSheet(Base, UUIDPKMixin, TimestampMixin):
    __tablename__ = "sideline_sheets"

    game_plan_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("game_plans.id"))
    version: Mapped[int] = mapped_column(default=1)
    is_final: Mapped[bool] = mapped_column(Boolean, default=False)


class SidelineSheetEntry(Base, UUIDPKMixin):
    __tablename__ = "sideline_sheet_entries"

    sideline_sheet_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("sideline_sheets.id"))
    play_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("plays.id"))
    down_distance_bucket: Mapped[DownDistanceBucket] = mapped_column(Enum(DownDistanceBucket))
    field_zone: Mapped[FieldZone | None] = mapped_column(Enum(FieldZone), nullable=True)
    hash_position: Mapped[HashPosition | None] = mapped_column(Enum(HashPosition), nullable=True)
    priority_tag_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("tags.id"), nullable=True)
    sort_order: Mapped[int]
    notes: Mapped[str | None] = mapped_column(String(1000), nullable=True)
