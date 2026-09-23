import uuid

from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.models.base import UUIDPKMixin
from app.models.enums import PlayType, SideOfBall, TagCategory


class PersonnelGroup(Base, UUIDPKMixin):
    __tablename__ = "personnel_groups"

    team_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("teams.id"), nullable=True)
    label: Mapped[str] = mapped_column(String(50))
    rb_count: Mapped[int]
    te_count: Mapped[int]
    wr_count: Mapped[int]


class Formation(Base, UUIDPKMixin):
    __tablename__ = "formations"

    personnel_group_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("personnel_groups.id"))
    name: Mapped[str] = mapped_column(String(255))
    side_of_ball: Mapped[SideOfBall] = mapped_column(Enum(SideOfBall))
    diagram_url: Mapped[str | None] = mapped_column(String(1000), nullable=True)


class Play(Base, UUIDPKMixin):
    __tablename__ = "plays"

    formation_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("formations.id"))
    game_plan_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("game_plans.id"), nullable=True)
    name: Mapped[str] = mapped_column(String(255))
    play_type: Mapped[PlayType] = mapped_column(Enum(PlayType))
    call_sheet_text: Mapped[str] = mapped_column(String(500))
    diagram_url: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    notes: Mapped[str | None] = mapped_column(String(2000), nullable=True)


class Tag(Base, UUIDPKMixin):
    __tablename__ = "tags"

    category: Mapped[TagCategory] = mapped_column(Enum(TagCategory))
    label: Mapped[str] = mapped_column(String(100))


class PlayTag(Base, UUIDPKMixin):
    __tablename__ = "play_tags"

    play_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("plays.id"))
    tag_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("tags.id"))
