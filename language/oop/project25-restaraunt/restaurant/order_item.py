from decimal import Decimal
from .menu_item import MenuItem
from .validators import validate_quantity

class OrderItem:
    """A menu item and its quantity in an order."""
    def __init__(self, menu_item: MenuItem, quantity: int):
        if not isinstance(menu_item, MenuItem):
            raise TypeError("menu_item must be a MenuItem instance.")
        self.__menu_item = menu_item
        self.__quantity = validate_quantity(quantity)

    @property
    def menu_item(self) -> MenuItem:
        return self.__menu_item

    @property
    def quantity(self) -> int:
        return self.__quantity

    def update_quantity(self, quantity: int) -> None:
        self.__quantity = validate_quantity(quantity)

    @property
    def line_total(self) -> Decimal:
        return self.menu_item.price * self.quantity

    def __str__(self) -> str:
        return (f"{self.menu_item.name} x {self.quantity} "
                f"@ ₦{self.menu_item.price:,.2f} = ₦{self.line_total:,.2f}")
