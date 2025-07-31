from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class RoomType:
    type: str
    price_per_night: Decimal
    max_guests: int

    @staticmethod
    def standard() -> "RoomType":
        return RoomType(type="STANDARD", price_per_night=Decimal("100.00"), max_guests=2)

    @staticmethod
    def deluxe() -> "RoomType":
        return RoomType(type="DELUXE", price_per_night=Decimal("200.00"), max_guests=3)

    @staticmethod
    def suite() -> "RoomType":
        return RoomType(type="SUITE", price_per_night=Decimal("300.00"), max_guests=4)