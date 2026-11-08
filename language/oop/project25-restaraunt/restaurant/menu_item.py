from decimal import Decimal
from .validators import validate_name, validate_positive_amount

class MenuItem:
    """A menu product with an ID, name, and unit price."""
    def __init__(self, item_id: str, name: str, price: Decimal):
        self.__item_id = validate_name(item_id, "Item ID")
        self.__name = validate_name(name, "Menu item name")
        self.__price = validate_positive_amount(price)

    @property
    def item_id(self) -> str:
        return self.__item_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> Decimal:
        return self.__price

    def __str__(self) -> str:
        return f"{self.name} ({self.item_id}) — ₦{self.price:,.2f}"
