from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from uuid import uuid4


# =========================================================
# 1. SHARED DATA MODELS
# =========================================================

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


# =========================================================
# 2. USER: SHARED ACCOUNT BEHAVIOR ONLY
# =========================================================

class User:
    def __init__(self, user_name: str, email: str):
        self.__user_name = self._validate_name(user_name)
        self.__email = self._validate_email(email)
        self.__is_account_active = True

    @staticmethod
    def _validate_name(value: str) -> str:
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")

        value = value.strip()
        if not value:
            raise ValueError("Name cannot be empty.")

        return value

    @staticmethod
    def _validate_email(value: str) -> str:
        if not isinstance(value, str):
            raise TypeError("Email must be a string.")

        value = value.strip()
        if (
            not value
            or value.count("@") != 1
            or value.startswith("@")
            or value.endswith("@")
            or any(char.isspace() for char in value)
            or "." not in value.split("@")[1]
            or value.endswith(".")
        ):
            raise ValueError("Please provide a valid email address.")

        return value

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def email(self) -> str:
        return self.__email

    @property
    def is_account_active(self) -> bool:
        return self.__is_account_active

    def activate_account(self) -> None:
        self.__is_account_active = True

    def deactivate_account(self) -> None:
        self.__is_account_active = False

    def _ensure_active(self) -> None:
        if not self.is_account_active:
            raise PermissionError("This account is deactivated.")

    def display_user_information(self) -> str:
        status = "Active" if self.is_account_active else "Deactivated"
        return (
            "\n========== USER INFORMATION ==========\n"
            f"Name: {self.user_name}\n"
            f"Email: {self.email}\n"
            f"Account status: {status}\n"
            "======================================"
        )

    def __str__(self) -> str:
        return f"User({self.user_name!r}, {self.email!r})"


# =========================================================
# 3. CUSTOMER: SHOPPING, CART, CHECKOUT, AND STANDARD BENEFIT
# =========================================================

class Customer(User):
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
        # Product is frozen, so returning a tuple is safe.
        return tuple(self.__products)

    @property
    def transaction_history(self) -> tuple[Transaction, ...]:
        return tuple(self.__transaction_history)

    @staticmethod
    def _to_decimal(value) -> Decimal:
        if isinstance(value, bool) or not isinstance(
            value, (int, float, Decimal)
        ):
            raise TypeError("Amount must be an int, float, or Decimal.")

        try:
            result = Decimal(str(value))
        except (InvalidOperation, ValueError):
            raise ValueError("Amount must be a valid number.") from None

        if not result.is_finite():
            raise ValueError("Amount must be finite.")

        return result

    @classmethod
    def _validate_positive_amount(cls, value) -> Decimal:
        amount = cls._to_decimal(value)
        if amount <= Decimal("0"):
            raise ValueError("Amount must be greater than zero.")
        return amount

    @staticmethod
    def _validate_quantity(quantity: int) -> int:
        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        return quantity

    def add_product(
        self, name: str, quantity: int, unit_price
    ) -> str:
        self._ensure_active()

        if not isinstance(name, str):
            raise TypeError("Product name must be a string.")
        name = name.strip()
        if not name:
            raise ValueError("Product name cannot be empty.")

        quantity = self._validate_quantity(quantity)
        unit_price = self._validate_positive_amount(unit_price)

        product_id = f"PR-{uuid4().hex[:12].upper()}"
        self.__products.append(
            Product(product_id, name, quantity, unit_price)
        )
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
        return sum(
            (product.subtotal for product in self.__products),
            Decimal("0"),
        )

    def cal_discount(self, subtotal: Decimal) -> Decimal:
        """Standard customers receive 5% off at the threshold."""
        subtotal = self._to_decimal(subtotal)

        if subtotal >= self.DISCOUNT_THRESHOLD:
            return subtotal * self.DISCOUNT_RATE

        return Decimal("0")

    def cal_final_price(self) -> dict[str, Decimal]:
        subtotal = self.cal_subtotal()

        # Enforce the invariant that a discount cannot be negative
        # or greater than the subtotal, even if a subclass is incorrect.
        discount = self._to_decimal(self.cal_discount(subtotal))
        discount = min(max(discount, Decimal("0")), subtotal)

        discounted_subtotal = subtotal - discount
        vat = (discounted_subtotal * self.VAT_RATE).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        total = discounted_subtotal + vat

        return {
            "subtotal": subtotal,
            "discount": discount,
            "vat": vat,
            "total": total,
        }

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
        for product in self.__products:
            lines.append(
                f"{product.product_id} | {product.name} | "
                f"Qty: {product.quantity} | "
                f"Unit: ₦{product.unit_price:,.2f} | "
                f"Subtotal: ₦{product.subtotal:,.2f}"
            )

        lines.append(f"Cart subtotal: ₦{self.cal_subtotal():,.2f}")
        lines.append("===================================")
        return "\n".join(lines)

    def display_transaction_history(self) -> str:
        if not self.__transaction_history:
            return "No completed transactions."

        lines = ["\n========== TRANSACTION HISTORY =========="]
        for transaction in self.__transaction_history:
            lines.append(
                f"{transaction.transaction_id} | "
                f"{transaction.customer_type} | "
                f"Total: ₦{transaction.total:,.2f}"
            )
        lines.append("==========================================")
        return "\n".join(lines)

    def display_user_information(self) -> str:
        # Extend, rather than duplicate, the parent implementation.
        return (
            f"{super().display_user_information()}\n"
            f"Customer ID: {self.customer_id}\n"
            f"Customer type: {self.customer_type}"
        )

    def __str__(self) -> str:
        return (
            f"{self.customer_type} customer "
            f"{self.user_name!r} ({self.customer_id})"
        )


# =========================================================
# 4. PREMIUM CUSTOMER: PREMIUM BENEFITS
# =========================================================

class PremiumCustomer(Customer):
    DISCOUNT_RATE = Decimal("0.10")

    def __init__(self, user_name: str, email: str):
        super().__init__(user_name, email)
        self.__membership_level = "Gold"

    @property
    def customer_type(self) -> str:
        return "Premium"

    @property
    def membership_level(self) -> str:
        return self.__membership_level

    def cal_discount(self, subtotal: Decimal) -> Decimal:
        subtotal = self._to_decimal(subtotal)

        if subtotal <= Decimal("0"):
            return Decimal("0")

        # Premium customers receive 10% off positive subtotals.
        return subtotal * self.DISCOUNT_RATE

    def display_user_information(self) -> str:
        return (
            f"{super().display_user_information()}\n"
            f"Membership level: {self.membership_level}\n"
            "Premium benefit: 10% discount on eligible purchases"
        )


# =========================================================
# 5. BUSINESS CUSTOMER: BUSINESS IDENTITY AND BULK BENEFITS
# =========================================================

class BusinessCustomer(Customer):
    DISCOUNT_THRESHOLD = Decimal("10000")
    DISCOUNT_RATE = Decimal("0.15")

    def __init__(
        self,
        user_name: str,
        email: str,
        business_name: str,
        registration_number: str,
    ):
        super().__init__(user_name, email)

        if not isinstance(business_name, str):
            raise TypeError("Business name must be a string.")
        business_name = business_name.strip()
        if not business_name:
            raise ValueError("Business name cannot be empty.")

        if not isinstance(registration_number, str):
            raise TypeError("Registration number must be a string.")
        registration_number = registration_number.strip()
        if not registration_number:
            raise ValueError("Registration number cannot be empty.")

        self.__business_name = business_name
        self.__registration_number = registration_number

    @property
    def customer_type(self) -> str:
        return "Business"

    @property
    def business_name(self) -> str:
        return self.__business_name

    @property
    def registration_number(self) -> str:
        return self.__registration_number

    def cal_discount(self, subtotal: Decimal) -> Decimal:
        subtotal = self._to_decimal(subtotal)

        if subtotal >= self.DISCOUNT_THRESHOLD:
            return subtotal * self.DISCOUNT_RATE

        return Decimal("0")

    def display_user_information(self) -> str:
        return (
            f"{super().display_user_information()}\n"
            f"Business name: {self.business_name}\n"
            f"Registration number: {self.registration_number}\n"
            "Business benefit: 15% discount on purchases of ₦10,000 or more"
        )


# =========================================================
# 6. DEMONSTRATION AND TESTS
# =========================================================

def show_price_summary(customer: Customer) -> None:
    amounts = customer.cal_final_price()
    print(f"\n{customer.customer_type} price summary")
    print(f"Subtotal: ₦{amounts['subtotal']:,.2f}")
    print(f"Discount: ₦{amounts['discount']:,.2f}")
    print(f"VAT:      ₦{amounts['vat']:,.2f}")
    print(f"Total:    ₦{amounts['total']:,.2f}")


def main() -> None:
    standard = Customer("John Doe", "john@example.com")
    premium = PremiumCustomer("Mary Jane", "mary@example.com")
    business = BusinessCustomer(
        "Ada Okafor",
        "ada@company.example",
        "ABC Office Supplies Ltd",
        "RC-123456",
    )

    # Inherited and specialized details.
    print(standard.display_user_information())
    print(premium.display_user_information())
    print(business.display_user_information())

    # Use the same cart and checkout interface for every customer.
    standard.add_product("Laptop", 1, Decimal("3500.00"))
    standard.add_product("Mouse", 2, Decimal("300.00"))

    premium.add_product("Phone", 1, Decimal("5000.00"))
    business.add_product("Office Chairs", 2, Decimal("6000.00"))

    print(standard.display_cart())
    show_price_summary(standard)
    show_price_summary(premium)
    show_price_summary(business)

    transaction = standard.checkout()
    print("\nCompleted transaction:", transaction)
    print(standard.display_transaction_history())

    # Demonstrate the inheritance relationships.
    print("\nInheritance checks")
    print("Premium is a Customer:", isinstance(premium, Customer))
    print("Business is a User:", isinstance(business, User))
    print(
        "PremiumCustomer subclasses Customer:",
        issubclass(PremiumCustomer, Customer),
    )

    # Invalid amount and quantity examples.
    print("\nValidation checks")
    for bad_price in (0, -10, True, float("inf"), float("nan")):
        try:
            standard.add_product("Invalid Item", 1, bad_price)
        except (TypeError, ValueError) as error:
            print(f"Rejected price {bad_price!r}: {error}")

    try:
        standard.add_product("Invalid Quantity", True, 100)
    except (TypeError, ValueError) as error:
        print(f"Rejected quantity: {error}")

    # Deactivated accounts cannot change their carts or checkout.
    standard.deactivate_account()
    try:
        standard.add_product("Another Item", 1, 100)
    except PermissionError as error:
        print(f"Deactivated account blocked: {error}")


if __name__ == "__main__":
    main()
