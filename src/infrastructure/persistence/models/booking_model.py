from sqlalchemy import Column, String, Enum, DateTime
from .database import Base
from ..domain.entities.booking import BookingStatus

class BookingModel(Base):
    __tablename__ = "bookings"
    booking_id = Column(String, primary_key=True)
    reference = Column(String, unique=True, nullable=False)
    guest_id = Column(String, nullable=False)
    room_id = Column(String, nullable=False)
    check_in = Column(DateTime, nullable=False)
    check_out = Column(DateTime, nullable=False)
    payment_amount = Column(String, nullable=False)
    payment_status = Column(String, nullable=False)
    status = Column(Enum(BookingStatus), nullable=False)