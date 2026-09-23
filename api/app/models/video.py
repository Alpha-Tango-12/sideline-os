import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.models.base import UUIDPKMixin
from app.models.enums import ClipSource


class VideoClip(Base, UUIDPKMixin):
    __tablename__ = "video_clips"

    game_plan_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("game_plans.id"), nullable=True)
    source: Mapped[ClipSource] = mapped_column(Enum(ClipSource))
    storage_url: Mapped[str] = mapped_column(String(2000))
    duration_seconds: Mapped[float | None] = mapped_column(nullable=True)
    formation_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("formations.id"), nullable=True)
    opponent_context: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class ClipTag(Base, UUIDPKMixin):
    __tablename__ = "clip_tags"

    clip_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("video_clips.id"))
    tag_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("tags.id"))


class ClipPlayLink(Base, UUIDPKMixin):
    __tablename__ = "clip_play_links"

    clip_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("video_clips.id"))
    play_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("plays.id"))


class ClipAnnotation(Base, UUIDPKMixin):
    __tablename__ = "clip_annotations"

    clip_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("video_clips.id"))
    author_staff_member_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("staff_members.id"))
    timestamp_seconds: Mapped[float]
    note_text: Mapped[str] = mapped_column(String(2000))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
