import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.models.base import UUIDPKMixin
from app.models.enums import PushedEntityType, TargetAudience


class PushRecord(Base, UUIDPKMixin):
    __tablename__ = "push_records"

    game_plan_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("game_plans.id"))
    pushed_entity_type: Mapped[PushedEntityType] = mapped_column(Enum(PushedEntityType))
    pushed_entity_id: Mapped[uuid.UUID]
    version: Mapped[int]
    pushed_by_staff_member_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("staff_members.id"))
    pushed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    target_audience: Mapped[TargetAudience] = mapped_column(Enum(TargetAudience))


class DeviceAckReceipt(Base, UUIDPKMixin):
    __tablename__ = "device_ack_receipts"

    push_record_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("push_records.id"))
    device_id: Mapped[str] = mapped_column(String(255))
    fetched_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    viewed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
