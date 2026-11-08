from validators import validate_positive_quantity


class CartItem:
    def __init__(self, product, quantity=1):
        self.product = product
        self.quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = validate_positive_quantity(value)

    @property
    def unit_price(self):
        return self.product.price

    @property
    def subtotal(self):
        return self.unit_price * self.quantity

    def __str__(self):
        return f"{self.product.name} x {self.quantity} = ₦{self.subtotal:.2f}"

    def __repr__(self):
        return f"CartItem(product={self.product.name!r}, quantity={self.quantity})"
