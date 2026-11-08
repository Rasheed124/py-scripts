from decimal import Decimal
from validators import validate_positive_quantity
from cart.cart_item import CartItem


class ShoppingCart:
    DISCOUNT_RATE = Decimal("0.10")
    DISCOUNT_THRESHOLD = Decimal("100000.00")

    def __init__(self):
        self._items = {}

    @property
    def items(self):
        return tuple(self._items.values())

    @property
    def subtotal(self):
        return sum((item.subtotal for item in self._items.values()), Decimal("0.00"))

    @property
    def discount(self):
        return (self.subtotal * self.DISCOUNT_RATE).quantize(Decimal("0.01")) \
            if self.subtotal >= self.DISCOUNT_THRESHOLD else Decimal("0.00")

    @property
    def total(self):
        return self.subtotal - self.discount

    @property
    def is_empty(self):
        return not self._items

    def add_item(self, product, quantity=1):
        quantity = validate_positive_quantity(quantity)
        existing = self._items.get(product.product_id)
        new_quantity = quantity + (existing.quantity if existing else 0)
        if new_quantity > product.stock:
            raise ValueError(f"Cannot add {new_quantity} {product.name}(s); only {product.stock} in stock.")
        if existing:
            existing.quantity = new_quantity
        else:
            self._items[product.product_id] = CartItem(product, quantity)

    def remove_item(self, product_or_id):
        product_id = getattr(product_or_id, "product_id", product_or_id)
        if product_id not in self._items:
            raise KeyError("Product is not in the cart.")
        del self._items[product_id]

    def update_quantity(self, product_or_id, quantity):
        quantity = validate_positive_quantity(quantity)
        product_id = getattr(product_or_id, "product_id", product_or_id)
        if product_id not in self._items:
            raise KeyError("Product is not in the cart.")
        item = self._items[product_id]
        if quantity > item.product.stock:
            raise ValueError(f"Only {item.product.stock} {item.product.name}(s) in stock.")
        item.quantity = quantity

    def validate_stock(self):
        for item in self._items.values():
            if item.quantity > item.product.stock:
                raise ValueError(f"Insufficient stock for {item.product.name}: requested {item.quantity}, available {item.product.stock}.")

    def clear(self):
        self._items.clear()

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self.items)

    def __str__(self):
        if self.is_empty:
            return "Shopping cart is empty."
        lines = [str(item) for item in self._items.values()]
        lines.extend([f"Subtotal: ₦{self.subtotal:.2f}", f"Discount: ₦{self.discount:.2f}", f"Total: ₦{self.total:.2f}"])
        return "\n".join(lines)

    def __repr__(self):
        return f"ShoppingCart(items={len(self)})"
