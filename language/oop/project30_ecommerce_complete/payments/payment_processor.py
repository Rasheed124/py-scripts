from abc import ABC, abstractmethod
from decimal import Decimal


class PaymentProcessor(ABC):
    @property
    @abstractmethod
    def method_name(self):
        raise NotImplementedError

    @abstractmethod
    def pay(self, amount: Decimal) -> bool:
        """Return True for simulated success, False for simulated failure."""
        raise NotImplementedError
