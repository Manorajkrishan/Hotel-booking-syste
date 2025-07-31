from sqlalchemy import Column, String, Integer
from uuid import UUID
from .database import Base

class GuestModel(Base):
    __tablename__ = "guests"
    guest_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)