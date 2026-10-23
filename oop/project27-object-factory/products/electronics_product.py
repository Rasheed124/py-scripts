from .product import Product
from .validators import validate_non_negative_int


class ElectronicsProduct(Product):
    """Product subtype with a warranty period measured in months."""

    def __init__(self, name, price, quantity: int, warranty_months: int):
        super().__init__(name, price, quantity)
        self.__warranty_months = validate_non_negative_int(warranty_months, "Warranty months")

    @property
    def warranty_months(self) -> int:
        return self.__warranty_months

    @classmethod
    def from_dict(cls, data: dict):
        if not isinstance(data, dict):
            raise TypeError("Electronics product data must be a dictionary.")
        required = {"name", "price", "quantity", "warranty_months"}
        missing = required - data.keys()
        if missing:
            raise ValueError(f"Missing required field(s): {', '.join(sorted(missing))}.")
        return cls(
            name=data["name"],
            price=data["price"],
            quantity=data["quantity"],
            warranty_months=data["warranty_months"],
        )

    @classmethod
    def from_string(cls, product_string: str):
        """Parse 'name,price,quantity,warranty_months'."""
        if not isinstance(product_string, str):
            raise TypeError("Electronics product data must be a string.")
        parts = [part.strip() for part in product_string.split(",")]
        if len(parts) != 4:
            raise ValueError("Expected format: name,price,quantity,warranty_months.")
        name, price_text, quantity_text, warranty_text = parts
        if not all((name, price_text, quantity_text, warranty_text)):
            raise ValueError("All electronics product fields are required.")
        try:
            quantity = int(quantity_text)
            warranty_months = int(warranty_text)
        except ValueError:
            raise ValueError("Quantity and warranty must be integers.") from None
        return cls(
            name=name,
            price=price_text,
            quantity=quantity,
            warranty_months=warranty_months,
        )

    def __str__(self) -> str:
        return (
            f"ElectronicsProduct(name={self.name!r}, price={self.price:.2f}, "
            f"quantity={self.quantity}, warranty_months={self.warranty_months})"
        )
