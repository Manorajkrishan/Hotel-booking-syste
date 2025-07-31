from dataclasses import dataclass
from decimal import Decimal
from enum import Enum

class PaymentStatus(Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

@dataclass
class Payment:
    amount: Decimal
    status: PaymentStatus