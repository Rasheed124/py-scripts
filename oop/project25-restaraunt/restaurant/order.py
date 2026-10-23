from decimal import Decimal, ROUND_HALF_UP
from uuid import uuid4
from .customer import Customer
from .order_item import OrderItem

class Order:
    """Owns order items and calculates current totals."""
    DISCOUNT_THRESHOLD = Decimal("20000.00")
    DISCOUNT_RATE = Decimal("0.10")

    def __init__(self, customer: Customer):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance.")
        self.__order_id = str(uuid4())[:8].upper()
        self.__customer = customer
        self.__items: dict[str, OrderItem] = {}

    @property
    def order_id(self) -> str:
        return self.__order_id

    @property
    def customer(self) -> Customer:
        return self.__customer

    @property
    def items(self) -> tuple[OrderItem, ...]:
        return tuple(self.__items.values())

    def add_item(self, order_item: OrderItem) -> None:
        if not isinstance(order_item, OrderItem):
            raise TypeError("order_item must be an OrderItem instance.")
        item_id = order_item.menu_item.item_id
        if item_id in self.__items:
            existing = self.__items[item_id]
            existing.update_quantity(existing.quantity + order_item.quantity)
        else:
            self.__items[item_id] = order_item

    def update_quantity(self, item_id: str, quantity: int) -> None:
        if item_id not in self.__items:
            raise KeyError(f"Item {item_id!r} is not in this order.")
        self.__items[item_id].update_quantity(quantity)

    def remove_item(self, item_id: str) -> None:
        try:
            del self.__items[item_id]
        except KeyError:
            raise KeyError(f"Item {item_id!r} is not in this order.") from None

    @property
    def subtotal(self) -> Decimal:
        return sum((item.line_total for item in self.__items.values()), Decimal("0.00"))

    @property
    def discount_rate(self) -> Decimal:
        return self.DISCOUNT_RATE if self.subtotal >= self.DISCOUNT_THRESHOLD else Decimal("0")

    @property
    def discount_amount(self) -> Decimal:
        return (self.subtotal * self.discount_rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    @property
    def total(self) -> Decimal:
        return (self.subtotal - self.discount_amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def generate_receipt(self) -> str:
        lines = [
            "=" * 48, "RESTAURANT ORDER RECEIPT", "=" * 48,
            f"Order ID: {self.order_id}",
            f"Customer: {self.customer.name}",
            f"Email: {self.customer.email}",
            "-" * 48,
        ]
        if not self.__items:
            lines.append("No items in this order.")
        else:
            lines.extend(str(item) for item in self.__items.values())
        lines.extend([
            "-" * 48,
            f"Subtotal:        ₦{self.subtotal:,.2f}",
            f"Discount ({self.discount_rate * 100:.0f}%):  -₦{self.discount_amount:,.2f}",
            f"TOTAL:           ₦{self.total:,.2f}",
            "=" * 48,
        ])
        return "\n".join(lines)
