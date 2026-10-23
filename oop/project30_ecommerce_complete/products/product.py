from uuid import uuid4
from validators import validate_non_empty_string, validate_price, validate_stock


class Product:
    def __init__(self, name, price, stock, category="General"):
        self._product_id = str(uuid4())
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = validate_non_empty_string(value, "Product name")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = validate_price(value)

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        self._stock = validate_stock(value)

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = validate_non_empty_string(value, "Category")

    def reduce_stock(self, quantity):
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if quantity > self.stock:
            raise ValueError(f"Not enough stock for {self.name}. Available: {self.stock}.")
        self._stock -= quantity

    def increase_stock(self, quantity):
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self._stock += quantity

    def __str__(self):
        return f"{self.name} — ₦{self.price:.2f} ({self.stock} in stock)"

    def __repr__(self):
        return f"Product(product_id={self.product_id!r}, name={self.name!r}, price={self.price!r})"
