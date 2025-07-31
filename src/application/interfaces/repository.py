from abc import ABC, abstractmethod
from uuid import UUID
from ..domain.entities.guest import Guest
from ..domain.entities.room import Room
from ..domain.entities.booking import Booking
from ..domain.value_objects.date_range import DateRange

class IBookingRepository(ABC):
    @abstractmethod
    async def save(self, booking: Booking) -> None:
        pass

    @abstractmethod
    async def get_guest(self, guest_id: UUID) -> Guest:
        pass

class IRoomRepository(ABC):
    @abstractmethod
    async def get_room(self, room_id: UUID) -> Room:
        pass

    @abstractmethod
    async def find_available_rooms(self, date_range: DateRange) -> list[Room]:
        pass