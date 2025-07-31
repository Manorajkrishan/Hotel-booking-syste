from abc import ABC, abstractmethod
from decimal import Decimal
from ..domain.value_objects.payment import Payment

class IPaymentService(ABC):
    @abstractmethod
    async def process_payment(self, amount: Decimal) -> Payment:
        pass