from decimal import Decimal, ROUND_HALF_UP
from uuid import uuid4

from .models import Product, Transaction
from .user import User
from .validators import to_decimal, validate_name, validate_positive_amount, validate_quantity

class Customer(User):
    """Standard customer: cart, checkout, purchase history, and discount."""
    VAT_RATE = Decimal("0.075")
    DISCOUNT_THRESHOLD = Decimal("4000")
    DISCOUNT_RATE = Decimal("0.05")

    def __init__(self, user_name: str, email: str):
        super().__init__(user_name, email)
        self.__customer_id = f"CUST-{uuid4().hex[:12].upper()}"
        self.__products: list[Product] = []
        self.__transaction_history: list[Transaction] = []

    @property
    def customer_id(self) -> str:
        return self.__customer_id

    @property
    def customer_type(self) -> str:
        return "Standard"

    @property
    def products(self) -> tuple[Product, ...]:
        return tuple(self.__products)

    @property
    def transaction_history(self) -> tuple[Transaction, ...]:
        return tuple(self.__transaction_history)

    def add_product(self, name: str, quantity: int, unit_price) -> str:
        self._ensure_active()
        name = validate_name(name, "Product name")
        quantity = validate_quantity(quantity)
        unit_price = validate_positive_amount(unit_price)
        product_id = f"PR-{uuid4().hex[:12].upper()}"
        self.__products.append(Product(product_id, name, quantity, unit_price))
        return product_id

    def remove_product(self, product_id: str) -> bool:
        self._ensure_active()
        for index, product in enumerate(self.__products):
            if product.product_id == product_id:
                del self.__products[index]
                return True
        return False

    def clear_cart(self) -> None:
        self._ensure_active()
        self.__products.clear()

    def cal_subtotal(self) -> Decimal:
        return sum((p.subtotal for p in self.__products), Decimal("0"))

    def cal_discount(self, subtotal: Decimal) -> Decimal:
        subtotal = to_decimal(subtotal)
        return subtotal * self.DISCOUNT_RATE if subtotal >= self.DISCOUNT_THRESHOLD else Decimal("0")

    def cal_final_price(self) -> dict[str, Decimal]:
        subtotal = self.cal_subtotal()
        discount = to_decimal(self.cal_discount(subtotal))
        discount = min(max(discount, Decimal("0")), subtotal)
        discounted = subtotal - discount
        vat = (discounted * self.VAT_RATE).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        return {"subtotal": subtotal, "discount": discount, "vat": vat, "total": discounted + vat}

    def checkout(self) -> Transaction:
        self._ensure_active()
        if not self.__products:
            raise ValueError("Cannot checkout an empty cart.")
        amounts = self.cal_final_price()
        transaction = Transaction(
            transaction_id=f"TX-{uuid4().hex[:16].upper()}",
            customer_id=self.customer_id,
            customer_type=self.customer_type,
            subtotal=amounts["subtotal"],
            discount=amounts["discount"],
            vat=amounts["vat"],
            total=amounts["total"],
        )
        self.__transaction_history.append(transaction)
        self.__products.clear()
        return transaction

    def display_cart(self) -> str:
        if not self.__products:
            return "Your shopping cart is empty."
        lines = ["\n========== SHOPPING CART =========="]
        for p in self.__products:
            lines.append(f"{p.product_id} | {p.name} | Qty: {p.quantity} | Unit: ₦{p.unit_price:,.2f} | Subtotal: ₦{p.subtotal:,.2f}")
        lines.append(f"Cart subtotal: ₦{self.cal_subtotal():,.2f}")
        lines.append("===================================")
        return "\n".join(lines)

    def display_transaction_history(self) -> str:
        if not self.__transaction_history:
            return "No completed transactions."
        lines = ["\n========== TRANSACTION HISTORY =========="]
        for t in self.__transaction_history:
            lines.append(f"{t.transaction_id} | {t.customer_type} | Total: ₦{t.total:,.2f}")
        lines.append("==========================================")
        return "\n".join(lines)

    def display_user_information(self) -> str:
        return f"{super().display_user_information()}\nCustomer ID: {self.customer_id}\nCustomer type: {self.customer_type}"

    def __str__(self) -> str:
        return f"{self.customer_type} customer {self.user_name!r} ({self.customer_id})"
