from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum
from uuid import uuid4


class OrderStatus(str, Enum):
    PENDING_PAYMENT = "pending_payment"
    CONFIRMED = "confirmed"
    PAYMENT_FAILED = "payment_failed"


class PaymentStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    FAILED = "failed"


class Order:
    DISCOUNT_RATE = Decimal("0.10")
    DISCOUNT_THRESHOLD = Decimal("100000.00")

    def __init__(self, customer, cart):
        if cart.is_empty:
            raise ValueError("Cannot create an order from an empty cart.")
        cart.validate_stock()
        self._order_id = str(uuid4())
        self.customer_id = customer.customer_id
        self.customer_name = customer.name
        self.shipping_address = customer.shipping_address
        self._lines = tuple({
            "product_id": item.product.product_id, "product_name": item.product.name,
            "unit_price": item.product.price, "quantity": item.quantity, "subtotal": item.subtotal,
        } for item in cart.items)
        self.subtotal = sum((line["subtotal"] for line in self._lines), Decimal("0.00"))
        self.discount = (self.subtotal * self.DISCOUNT_RATE).quantize(Decimal("0.01")) \
            if self.subtotal >= self.DISCOUNT_THRESHOLD else Decimal("0.00")
        self.total = self.subtotal - self.discount
        self.status = OrderStatus.PENDING_PAYMENT
        self.payment_status = PaymentStatus.PENDING
        self.payment_method = None
        self.created_at = datetime.now(timezone.utc)

    @property
    def order_id(self):
        return self._order_id

    @property
    def lines(self):
        return tuple(dict(line) for line in self._lines)

    def mark_paid(self, payment_method):
        self.payment_status = PaymentStatus.PAID
        self.status = OrderStatus.CONFIRMED
        self.payment_method = payment_method

    def mark_payment_failed(self, payment_method):
        self.payment_status = PaymentStatus.FAILED
        self.status = OrderStatus.PAYMENT_FAILED
        self.payment_method = payment_method

    def summary(self):
        return {
            "order_id": self.order_id, "customer_id": self.customer_id,
            "customer_name": self.customer_name, "lines": self.lines,
            "subtotal": self.subtotal, "discount": self.discount, "total": self.total,
            "status": self.status.value, "payment_status": self.payment_status.value,
            "payment_method": self.payment_method, "created_at": self.created_at.isoformat(),
        }

    def __str__(self):
        return f"Order {self.order_id[:8]} | {self.status.value} | Total ₦{self.total:.2f}"

    def __repr__(self):
        return f"Order(order_id={self.order_id!r}, total={self.total!r}, status={self.status.value!r})"
