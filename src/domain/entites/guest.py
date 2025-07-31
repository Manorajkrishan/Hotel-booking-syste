from uuid import UUID
from dataclasses import dataclass

@dataclass
class Guest:
    guest_id: UUID
    name: str
    age: int

    def is_eligible(self) -> bool:
        return self.age >= 18