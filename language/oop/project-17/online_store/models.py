from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class Product:
    product_id: str
    name: str
    quantity: int
    unit_price: Decimal

    @property
    def subtotal(self) -> Decimal:
        return self.unit_price * self.quantity

@dataclass(frozen=True)
class Transaction:
    transaction_id: str
    customer_id: str
    customer_type: str
    subtotal: Decimal
    discount: Decimal
    vat: Decimal
    total: Decimal
