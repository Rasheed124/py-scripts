
from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from uuid import uuid4


# =========================================================
# 1. PRODUCT MODEL
# =========================================================

@dataclass
class Product:
    product_id: str
    name: str
    quantity: int
    unit_price: Decimal

    @property
    def subtotal(self) -> Decimal:
        return self.unit_price * self.quantity


# =========================================================
# 2. TRANSACTION MODEL
# =========================================================

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
# 3. ABSTRACT USER CLASS
# =========================================================

class User(ABC):
    VAT_RATE = Decimal("0.075")

    def __init__(self, user_name: str, email: str):
        self.__user_name = self._validate_name(user_name)
        self.__email = self._validate_email(email)
        self.__is_account_active = True

        # Each user owns their own cart and history.
        self.__product_list: list[Product] = []
        self.__transaction_history: list[Transaction] = []

    # ---------------- VALIDATION ----------------

    @staticmethod
    def _validate_name(user_name: str) -> str:
        if not isinstance(user_name, str):
            raise TypeError("User name must be a string.")

        user_name = user_name.strip()

        if not user_name:
            raise ValueError("User name cannot be empty.")

        return user_name

    @staticmethod
    def _validate_email(email: str) -> str:
        if not isinstance(email, str):
            raise TypeError("Email must be a string.")

        email = email.strip()

        if (
            not email
            or email.count("@") != 1
            or email.startswith("@")
            or email.endswith("@")
            or any(char.isspace() for char in email)
            or "." not in email.split("@")[1]
            or email.endswith(".")
        ):
            raise ValueError("Please provide a valid email address.")

        return email

    @staticmethod
    def _to_decimal(amount) -> Decimal:
        if isinstance(amount, bool) or not isinstance(
            amount, (int, float, Decimal)
        ):
            raise TypeError("Amount must be a number.")

        try:
            value = Decimal(str(amount))
        except (InvalidOperation, ValueError):
            raise ValueError("Amount must be a valid number.") from None

        if not value.is_finite():
            raise ValueError("Amount must be finite.")

        return value

    @classmethod
    def validate_amount(cls, amount) -> Decimal:
        value = cls._to_decimal(amount)

        if value <= Decimal("0"):
            raise ValueError("Amount must be greater than zero.")

        return value

    @staticmethod
    def _validate_quantity(quantity: int) -> int:
        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        return quantity

    # ---------------- PROPERTIES ----------------

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def user_email(self) -> str:
        return self.__email

    @property
    def is_account_active(self) -> bool:
        return self.__is_account_active

    @property
    def product_list(self) -> tuple[Product, ...]:
        # Prevent callers from directly changing the cart list.
        return tuple(self.__product_list)

    @property
    def transaction_history(self) -> tuple[Transaction, ...]:
        return tuple(self.__transaction_history)

    # ---------------- ACCOUNT MANAGEMENT ----------------

    def activate_account(self) -> None:
        self.__is_account_active = True

    def deactivate_account(self) -> None:
        self.__is_account_active = False

    def _ensure_active(self) -> None:
        if not self.is_account_active:
            raise PermissionError("This account is deactivated.")

    # ---------------- CUSTOMER TYPE ----------------

    @property
    @abstractmethod
    def customer_type(self) -> str:
        """Return the customer's category."""
        raise NotImplementedError

    @abstractmethod
    def cal_discount(self, subtotal: Decimal) -> Decimal:
        """Calculate the discount for this customer type."""
        raise NotImplementedError

    # ---------------- CART MANAGEMENT ----------------

    def add_product(
        self,
        name: str,
        quantity: int,
        price: int | float | Decimal,
    ) -> str:
        self._ensure_active()

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name cannot be empty.")

        quantity = self._validate_quantity(quantity)
        unit_price = self.validate_amount(price)

        product_id = f"PR-{uuid4().hex[:12].upper()}"

        product = Product(
            product_id=product_id,
            name=name.strip(),
            quantity=quantity,
            unit_price=unit_price,
        )

        self.__product_list.append(product)

        return product_id

    def remove_product(self, product_id: str) -> bool:
        self._ensure_active()

        for product in self.__product_list:
            if product.product_id == product_id:
                self.__product_list.remove(product)
                return True

        return False

    def empty_product_list(self) -> None:
        self._ensure_active()
        self.__product_list.clear()

    def display_product_list(self) -> str:
        if not self.__product_list:
            return "Your shopping cart is empty."

        lines = ["\n========== SHOPPING CART =========="]

        for product in self.__product_list:
            lines.append(
                f"ID: {product.product_id} | "
                f"Name: {product.name} | "
                f"Quantity: {product.quantity} | "
                f"Unit Price: {product.unit_price:.2f} | "
                f"Subtotal: {product.subtotal:.2f}"
            )

        lines.append(
            f"Cart subtotal: {self.cal_subtotal():.2f}"
        )
        lines.append("===================================")

        return "\n".join(lines)

    # ---------------- PRICE CALCULATIONS ----------------

    def cal_subtotal(self) -> Decimal:
        return sum(
            (product.subtotal for product in self.__product_list),
            Decimal("0"),
        )

    def cal_final_price(self) -> dict[str, Decimal]:
        subtotal = self.cal_subtotal()

        discount = self.cal_discount(subtotal)
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

    # ---------------- CHECKOUT ----------------

    def checkout(self) -> Transaction:
        self._ensure_active()

        if not self.__product_list:
            raise ValueError("Cannot checkout an empty cart.")

        amounts = self.cal_final_price()

        transaction = Transaction(
            transaction_id=f"TX-{uuid4().hex.upper()}",
            customer_id=self.customer_id,
            customer_type=self.customer_type,
            subtotal=amounts["subtotal"],
            discount=amounts["discount"],
            vat=amounts["vat"],
            total=amounts["total"],
        )

        self.__transaction_history.append(transaction)
        self.__product_list.clear()

        return transaction

    @property
    @abstractmethod
    def customer_id(self) -> str:
        """Return the customer's unique ID."""
        raise NotImplementedError

    # ---------------- DISPLAY ----------------

    def display_user_information(self) -> str:
        status = (
            "Activated"
            if self.is_account_active
            else "Deactivated"
        )

        return (
            "\n========== USER INFORMATION ==========\n"
            f"Name: {self.user_name}\n"
            f"Email: {self.user_email}\n"
            f"Customer ID: {self.customer_id}\n"
            f"Customer Type: {self.customer_type}\n"
            f"Account Status: {status}\n"
            "======================================"
        )

    def display_transaction_history(self) -> str:
        if not self.__transaction_history:
            return "No completed transactions."

        lines = ["\n========== TRANSACTION HISTORY =========="]

        for transaction in self.__transaction_history:
            lines.append(
                f"ID: {transaction.transaction_id} | "
                f"Type: {transaction.customer_type} | "
                f"Total: {transaction.total:.2f}"
            )

        lines.append("==========================================")

        return "\n".join(lines)

    def __str__(self) -> str:
        return (
            f"{self.customer_type} {self.user_name!r} "
            "has been created successfully."
        )


# =========================================================
# 4. STANDARD CUSTOMER
# =========================================================

class Customer(User):
    DISCOUNT_THRESHOLD = Decimal("4000")
    DISCOUNT_RATE = Decimal("0.05")

    def __init__(self, user_name: str, email: str):
        super().__init__(user_name, email)
        self.__customer_id = f"CUST-{uuid4().hex[:12].upper()}"

    @property
    def customer_id(self) -> str:
        return self.__customer_id

    @property
    def customer_type(self) -> str:
        return "Standard"

    def cal_discount(self, subtotal: Decimal) -> Decimal:
        subtotal = self._to_decimal(subtotal)

        if subtotal >= self.DISCOUNT_THRESHOLD:
            return subtotal * self.DISCOUNT_RATE

        return Decimal("0")


# =========================================================
# 5. PREMIUM CUSTOMER
# =========================================================

class PremiumCustomer(Customer):
    DISCOUNT_RATE = Decimal("0.10")

    @property
    def customer_type(self) -> str:
        return "Premium"

    def cal_discount(self, subtotal: Decimal) -> Decimal:
        subtotal = self._to_decimal(subtotal)

        if subtotal <= Decimal("0"):
            return Decimal("0")

        return subtotal * self.DISCOUNT_RATE


# =========================================================
# 6. BUSINESS CUSTOMER
# =========================================================

class BusinessCustomer(Customer):
    DISCOUNT_THRESHOLD = Decimal("10000")
    DISCOUNT_RATE = Decimal("0.15")

    @property
    def customer_type(self) -> str:
        return "Business"

    def cal_discount(self, subtotal: Decimal) -> Decimal:
        subtotal = self._to_decimal(subtotal)

        if subtotal >= self.DISCOUNT_THRESHOLD:
            return subtotal * self.DISCOUNT_RATE

        return Decimal("0")


# =========================================================
# 7. MAIN PROGRAM
# =========================================================

def main():
    # Create different customer types.
    customer = Customer("John Doe", "john@example.com")
    premium = PremiumCustomer("Mary Jane", "mary@example.com")
    business = BusinessCustomer("ABC Company", "sales@abc.com")

    # Display customer information.
    print(customer.display_user_information())
    print(premium.display_user_information())
    print(business.display_user_information())

    # Add products to the standard customer's cart.
    first_id = customer.add_product("Laptop", 1, "3500.00")
    customer.add_product("Mouse", 2, "300.00")

    print(customer.display_product_list())

    # Display the calculated totals.
    amounts = customer.cal_final_price()

    print("\n========== PRICE SUMMARY ==========")
    print(f"Subtotal: {amounts['subtotal']:.2f}")
    print(f"Discount: {amounts['discount']:.2f}")
    print(f"VAT:      {amounts['vat']:.2f}")
    print(f"Total:    {amounts['total']:.2f}")

    # Remove a product using its ID.
    # Uncomment to remove the laptop:
    # customer.remove_product(first_id)

    # Complete the purchase.
    transaction = customer.checkout()

    print("\n========== CHECKOUT SUCCESS ==========")
    print(f"Transaction ID: {transaction.transaction_id}")
    print(f"Customer ID:    {transaction.customer_id}")
    print(f"Customer Type:  {transaction.customer_type}")
    print(f"Total Paid:     {transaction.total:.2f}")

    # Show transaction history.
    print(customer.display_transaction_history())

    # Demonstrate different pricing behavior.
    premium.add_product("Phone", 1, "5000.00")
    business.add_product("Office Equipment", 2, "6000.00")

    print("\nPremium price:", premium.cal_final_price())
    print("Business price:", business.cal_final_price())


if __name__ == "__main__":
    main()
