import string
import random
from dataclasses import dataclass

@dataclass(frozen=True)
class BookingReference:
    value: str

    @staticmethod
    def generate() -> "BookingReference":
        chars = string.ascii_uppercase + string.digits
        value = "".join(random.choices(chars, k=10))
        return BookingReference(value=value)