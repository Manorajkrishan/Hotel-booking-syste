from uuid import uuid4
from datetime import datetime
from decimal import Decimal
from ..entities.guest import Guest
from ..entities.room import Room
from ..entities.booking import Booking, BookingStatus
from ..value_objects.booking_reference import BookingReference
from ..value_objects.date_range import DateRange
from ..value_objects.payment import Payment, PaymentStatus

class BookingService:
    async def create_booking(
        self, guest: Guest, room: Room, check_in: datetime, check_out: datetime, num_guests: int
    ) -> Booking:
        if not guest.is_eligible():
            raise ValueError("Guest must be at least 18 years old")
        if num_guests > room.room_type.max_guests:
            raise ValueError(f"Too many guests for {room.room_type.type} room")
        date_range = DateRange(check_in=check_in, check_out=check_out)
        if not date_range.is_valid():
            raise ValueError("Invalid date range")
        days = (check_out - check_in).days
        amount = room.room_type.price_per_night * Decimal(days)
        payment = Payment(amount=amount, status=PaymentStatus.PENDING)
        return Booking(
            booking_id=uuid4(),
            reference=BookingReference.generate(),
            guest_id=guest.guest_id,
            room_id=room.room_id,
            date_range=date_range,
            payment=payment,
            status=BookingStatus.CONFIRMED,
        )