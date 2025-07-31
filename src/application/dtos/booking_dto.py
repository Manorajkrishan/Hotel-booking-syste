from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from ..domain.entities.booking import Booking, BookingStatus

class BookingCreateDTO(BaseModel):
    guest_id: UUID
    room_id: UUID
    check_in: datetime
    check_out: datetime
    num_guests: int

class BookingDTO(BaseModel):
    booking_id: UUID
    reference: str
    guest_id: UUID
    room_id: UUID
    check_in: datetime
    check_out: datetime
    status: str

    @staticmethod
    def from_entity(booking: Booking) -> "BookingDTO":
        return BookingDTO(
            booking_id=booking.booking_id,
            reference=booking.reference.value,
            guest_id=booking.guest_id,
            room_id=booking.room_id,
            check_in=booking.date_range.check_in,
            check_out=booking.date_range.check_out,
            status=booking.status.value,
        )