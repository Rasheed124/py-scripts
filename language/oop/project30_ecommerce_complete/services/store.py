from cart.shopping_cart import ShoppingCart
from orders.order import Order
from notifications.email_notifier import EmailNotifier
from validators import validate_non_empty_string


class Store:
    def __init__(self, name, default_notifier=None):
        self.name = validate_non_empty_string(name, "Store name")
        self._customers = {}
        self._products = {}
        self._orders = {}
        self.default_notifier = default_notifier or EmailNotifier()

    @property
    def customers(self):
        return tuple(self._customers.values())

    @property
    def products(self):
        return tuple(self._products.values())

    @property
    def orders(self):
        return tuple(self._orders.values())

    def register_customer(self, customer):
        if customer.user_id in self._customers:
            raise ValueError("Customer is already registered.")
        if any(c.email.lower() == customer.email.lower() for c in self._customers.values()):
            raise ValueError("A customer with this email is already registered.")
        if customer.shopping_cart is None:
            customer.shopping_cart = ShoppingCart()
        self._customers[customer.user_id] = customer
        return customer

    def add_product(self, product):
        if product.product_id in self._products:
            raise ValueError("Product is already registered.")
        self._products[product.product_id] = product
        return product

    def get_product(self, product_id):
        if product_id not in self._products:
            raise KeyError(f"No product found with ID {product_id}.")
        return self._products[product_id]

    def get_customer(self, customer_id):
        if customer_id not in self._customers:
            raise KeyError(f"No customer found with ID {customer_id}.")
        return self._customers[customer_id]

    def notify(self, customer, message, notifier=None):
        selected = notifier or self.default_notifier
        send = getattr(selected, "send", None)
        if not callable(send):
            raise TypeError("Notifier must provide a callable send(customer, message) method.")
        return send(customer, message)

    def checkout(self, customer, payment_processor, notifier=None):
        if customer.user_id not in self._customers:
            raise ValueError("Customer must be registered with this store.")
        if not customer.is_active:
            raise ValueError("Inactive customers cannot check out.")
        cart = customer.shopping_cart
        if cart is None or cart.is_empty:
            raise ValueError("Cannot check out with an empty cart.")

        cart.validate_stock()
        order = Order(customer, cart)
        paid = payment_processor.pay(order.total)

        if not paid:
            order.mark_payment_failed(payment_processor.method_name)
            self._orders[order.order_id] = order
            return order

        cart.validate_stock()
        for item in cart.items:
            if item.quantity > item.product.stock:
                raise ValueError(f"Insufficient stock for {item.product.name}.")
        for item in cart.items:
            item.product.reduce_stock(item.quantity)

        order.mark_paid(payment_processor.method_name)
        customer.add_order(order)
        self._orders[order.order_id] = order
        cart.clear()

        try:
            self.notify(
                customer,
                f"Your order {order.order_id[:8]} is confirmed. Total paid: ₦{order.total:.2f}.",
                notifier,
            )
        except Exception as exc:
            print(f"[WARNING] Order succeeded, but notification failed: {exc}")
        return order

    def __len__(self):
        return len(self._products)

    def __str__(self):
        return f"{self.name}: {len(self._products)} products, {len(self._customers)} customers"
