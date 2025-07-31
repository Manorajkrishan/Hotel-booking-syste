from uuid import UUID
from datetime import datetime
from enum import Enum
from dataclasses import dataclass
from .value_objects.date_range import DateRange
from .value_objects.booking_reference import BookingReference
from .value_objects.payment import Payment

class BookingStatus(Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CHECKED_IN = "CHECKED_IN"
    CHECKED_OUT = "CHECKED_OUT"
    CANCELLED = "CANCELLED"

@dataclass
class Booking:
    booking_id: UUID
    reference: BookingReference
    guest_id: UUID
    room_id: UUID
    date_range: DateRange
    payment: Payment
    status: BookingStatus = BookingStatus.PENDING

    def can_cancel(self, current_time: datetime) -> bool:
        return (
            self.status == BookingStatus.CONFIRMED
            and (self.date_range.check_in - current_time).total_seconds() / 3600 >= 48
        )

    def check_in(self) -> None:
        if self.status == BookingStatus.CONFIRMED:
            self.status = BookingStatus.CHECKED_IN

    def check_out(self) -> None:
        if self.status == BookingStatus.CHECKED_IN:
            self.status = BookingStatus.CHECKED_OUT