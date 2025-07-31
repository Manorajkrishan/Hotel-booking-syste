from uuid import UUID
from dataclasses import dataclass
from .value_objects.room_type import RoomType
from .value_objects.date_range import DateRange

@dataclass
class Room:
    room_id: UUID
    room_number: str
    room_type: RoomType

    def is_available(self, date_range: DateRange, bookings: list["Booking"]) -> bool:
        for booking in bookings:
            if (
                booking.room_id == self.room_id
                and booking.status not in [BookingStatus.CANCELLED, BookingStatus.CHECKED_OUT]
                and self._overlaps(booking.date_range, date_range)
            ):
                return False
        return True

    def _overlaps(self, existing: DateRange, requested: DateRange) -> bool:
        return not (
            requested.check_out <= existing.check_in
            or requested.check_in >= existing.check_out
        )