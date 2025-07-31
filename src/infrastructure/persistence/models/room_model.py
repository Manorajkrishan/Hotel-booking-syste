from sqlalchemy import Column, String
from .database import Base

class RoomModel(Base):
    __tablename__ = "rooms"
    room_id = Column(String, primary_key=True)
    room_number = Column(String, nullable=False)
    room_type = Column(String, nullable=False)
    price_per_night = Column(String, nullable=False)
    max_guests = Column(Integer, nullable=False)