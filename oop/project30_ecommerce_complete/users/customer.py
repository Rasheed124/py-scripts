from users.user import User


class Customer(User):
    def __init__(self, name, email, phone, password, shipping_address):
        super().__init__(name, email, phone, password)
        self.shipping_address = shipping_address
        self.shopping_cart = None
        self._order_history = []

    @property
    def customer_id(self):
        return self.user_id

    @property
    def shipping_address(self):
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, value):
        from validators import validate_non_empty_string
        self._shipping_address = validate_non_empty_string(value, "Shipping address")

    @property
    def order_history(self):
        return tuple(self._order_history)

    def add_order(self, order):
        self._order_history.append(order)

    def __str__(self):
        return f"Customer: {self.name}"
