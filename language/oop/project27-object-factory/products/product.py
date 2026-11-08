from decimal import Decimal

from .validators import (
    validate_name,
    validate_positive_price,
    validate_quantity,
    to_decimal,
)


class Product:
    """Represents a product and provides alternative constructors."""

    def __init__(self, name: str, price, quantity: int):
        self.__name = validate_name(name)
        self.__price = validate_positive_price(price)
        self.__quantity = validate_quantity(quantity)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> Decimal:
        return self.__price

    @property
    def quantity(self) -> int:
        return self.__quantity

    @classmethod
    def from_dict(cls, data: dict):
        """Create an instance from {'name': ..., 'price': ..., 'quantity': ...}."""
        if not isinstance(data, dict):
            raise TypeError("Product data must be a dictionary.")
        required = {"name", "price", "quantity"}
        missing = required - data.keys()
        if missing:
            raise ValueError(f"Missing required field(s): {', '.join(sorted(missing))}.")
        return cls(name=data["name"], price=data["price"], quantity=data["quantity"])

    @classmethod
    def from_string(cls, product_string: str):
        """Parse 'name,price,quantity'; subclasses may extend the format."""
        if not isinstance(product_string, str):
            raise TypeError("Product data must be a string.")
        parts = [part.strip() for part in product_string.split(",")]
        if len(parts) != 3:
            raise ValueError("Expected format: name,price,quantity.")
        name, price_text, quantity_text = parts
        if not name or not price_text or not quantity_text:
            raise ValueError("Name, price, and quantity cannot be empty.")
        price = to_decimal(price_text)
        try:
            quantity = int(quantity_text)
        except ValueError:
            raise ValueError("Quantity in the string must be an integer.") from None
        return cls(name=name, price=price, quantity=quantity)

    @staticmethod
    def is_valid_price(price) -> bool:
        """Return True when price is a finite numeric value greater than zero."""
        try:
            return to_decimal(price) > Decimal("0")
        except (TypeError, ValueError):
            return False

    def calculate_stock_value(self) -> Decimal:
        """Calculate this product's total stock value."""
        return self.price * self.quantity

    def __str__(self) -> str:
        return (
            f"Product(name={self.name!r}, price={self.price:.2f}, "
            f"quantity={self.quantity})"
        )
