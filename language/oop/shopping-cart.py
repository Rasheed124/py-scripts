
# #  object collaboration composition-based design.

# import random
# import string


# class Product:
#     def __init__(self, name: str, price: int | float):
#         if not isinstance(name, str) or not name.strip():
#             raise ValueError("Product name cannot be empty.")

#         if isinstance(price, bool) or not isinstance(price, (int, float)) or price <= 0:
#             raise ValueError("Price must be a positive number.")

#         self.__name = name.strip()
#         self.__price = price

#     @property
#     def name(self) -> str:
#         return self.__name

#     @property
#     def price(self) -> int | float:
#         return self.__price

#     def product_details(self):
#         return f"This is {self.__name}, it costs {self.__price}"


# class ShoppingCart:
#     def __init__(self):
#         self.cart = {}

#     def add_to_cart(self, product: Product, quantity: int):
#         if not isinstance(product, Product):
#             raise TypeError("You must add a Product object.")

#         if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
#             raise ValueError("Quantity must be a positive integer.")

#         product_cart_id = self.generate_product_cart_id()

#         self.cart[product_cart_id] = {
#             "product_name": product.name,
#             "product_price": product.price,
#             "product_quantity": quantity
#         }

#         print("Product added to cart successfully.")

#         return product_cart_id

#     def remove_from_cart(self, cart_id: str, quantity: int):
#         if cart_id not in self.cart:
#             raise ValueError("Product does not exist in the cart.")

#         if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
#             raise ValueError("Quantity must be a positive integer.")

#         product = self.cart[cart_id]

#         if quantity >= product["product_quantity"]:
#             del self.cart[cart_id]
#             print("Product removed from cart successfully.")
#         else:
#             product["product_quantity"] -= quantity
#             print("Product quantity reduced successfully.")

#     def show_products_in_cart(self):
#         if not self.cart:
#             print("Your cart is empty.")
#             return

#         for product_id, details in self.cart.items():
#             print(f"Cart ID: {product_id}")
#             print(f"Product: {details['product_name']}")
#             print(f"Price: {details['product_price']}")
#             print(f"Quantity: {details['product_quantity']}")
#             print(f"Subtotal: {details['product_price'] * details['product_quantity']}")
#             print("-" * 30)

#     def generate_product_cart_id(self) -> str:
#         while True:
#             product_cart_id = "".join(
#                 random.choices(string.ascii_uppercase + string.digits, k=8)
#             )

#             if product_cart_id not in self.cart:
#                 return product_cart_id



# product1 = Product("Laptop", 1500)
# product2 = Product("Mouse", 25)

# cart = ShoppingCart()

# laptop_id = cart.add_to_cart(product1, 2)
# mouse_id = cart.add_to_cart(product2, 3)

# cart.remove_from_cart(laptop_id, 1)
# cart.remove_from_cart(laptop_id, 1)

# cart.show_products_in_cart()













from decimal import Decimal, InvalidOperation
from uuid import uuid4


class Product:
    def __init__(
        self,
        name: str,
        price: int | float | Decimal,
        product_id: str | None = None
    ):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name cannot be empty.")

        if isinstance(price, bool) or not isinstance(price, (int, float, Decimal) ):
            raise TypeError("Price must be a number.")

        try:
            validated_price = Decimal(str(price))
        except (InvalidOperation, ValueError):
            raise ValueError("Price must be a valid number.")

        if not validated_price.is_finite() or validated_price <= 0:
            raise ValueError("Price must be a finite positive number.")

        if product_id is not None:
            if not isinstance(product_id, str) or not product_id.strip():
                raise ValueError("Product ID must be a non-empty string.")
            product_id = product_id.strip()
        else:
            product_id = f"P-{uuid4().hex[:8].upper()}"

        self.__product_id = product_id
        self.__name = name.strip()
        self.__price = validated_price

    @property
    def product_id(self) -> str:
        return self.__product_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> Decimal:
        return self.__price

    def product_details(self) -> str:
        return (
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ₦{self.__price:.2f}"
        )

    def __str__(self):
        return self.product_details()


class ShoppingCart:
    def __init__(self):
        self.__items: dict[str, dict] = {}

    @staticmethod
    def __validate_quantity(quantity: int):
        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

    def add_to_cart(self, product: Product, quantity: int = 1):
        if not isinstance(product, Product):
            raise TypeError("You must add a Product object.")

        self.__validate_quantity(quantity)

        product_id = product.product_id

        if product_id in self.__items:
            existing_product = self.__items[product_id]["product"]

            if existing_product is not product:
                raise ValueError(
                    f"Product ID {product_id} is already assigned "
                    "to a different product."
                )

            self.__items[product_id]["quantity"] += quantity
        else:
            self.__items[product_id] = {
                "product": product,
                "quantity": quantity
            }

        print(f"Added {quantity} x {product.name} to the cart.")

    def update_quantity(self, product_id: str, new_quantity: int):
        if product_id not in self.__items:
            raise ValueError("Product ID does not exist in the cart.")

        self.__validate_quantity(new_quantity)

        self.__items[product_id]["quantity"] = new_quantity

        product = self.__items[product_id]["product"]
        print(f"Updated {product.name} quantity to {new_quantity}.")

    def remove_from_cart(
        self,
        product_id: str,
        quantity: int | None = None
    ):
        if product_id not in self.__items:
            raise ValueError("Product ID does not exist in the cart.")

        if quantity is None:
            product = self.__items[product_id]["product"]
            del self.__items[product_id]
            print(f"Removed {product.name} from the cart.")
            return

        self.__validate_quantity(quantity)

        current_quantity = self.__items[product_id]["quantity"]

        if quantity > current_quantity:
            raise ValueError(
                f"Cannot remove {quantity}; "
                f"only {current_quantity} available."
            )

        product = self.__items[product_id]["product"]
        remaining_quantity = current_quantity - quantity

        if remaining_quantity == 0:
            del self.__items[product_id]
            print(f"Removed {product.name} from the cart.")
        else:
            self.__items[product_id]["quantity"] = remaining_quantity
            print(
                f"Removed {quantity} x {product.name}. "
                f"Remaining quantity: {remaining_quantity}."
            )

    def calculate_subtotal(self, product_id: str) -> Decimal:
        if product_id not in self.__items:
            raise ValueError("Product ID does not exist in the cart.")

        item = self.__items[product_id]
        product = item["product"]
        quantity = item["quantity"]

        return product.price * quantity

    @property
    def total_quantity(self) -> int:
        return sum(
            item["quantity"]
            for item in self.__items.values()
        )

    @property
    def total(self) -> Decimal:
        # Always calculate from the current cart contents.
        return sum(
            (
                item["product"].price * item["quantity"]
                for item in self.__items.values()
            ),
            Decimal("0.00")
        )

    def show_products_in_cart(self):
        if not self.__items:
            print("Your cart is empty.")
            return

        print("\n" + "=" * 55)
        print("SHOPPING CART")
        print("=" * 55)

        for product_id, item in self.__items.items():
            product = item["product"]
            quantity = item["quantity"]
            subtotal = product.price * quantity

            print(f"Product ID: {product_id}")
            print(f"Product:    {product.name}")
            print(f"Price:      ₦{product.price:.2f}")
            print(f"Quantity:   {quantity}")
            print(f"Subtotal:   ₦{subtotal:.2f}")
            print("-" * 55)

        print(f"Total units: {self.total_quantity}")
        print(f"Cart total:  ₦{self.total:.2f}")
        print("=" * 55)




# ==================== TESTING ====================

product1 = Product("Laptop", 1500000)
product2 = Product("Mouse", 25000)
product3 = Product("Keyboard", 45000)

product4 = Product("Mouse", 25000)

cart = ShoppingCart()

# 1. Add products
print("\nADDING PRODUCTS")
cart.add_to_cart(product1, 2)
cart.add_to_cart(product2, 3)
cart.add_to_cart(product3, 1)
cart.add_to_cart(product4, 1)

cart.show_products_in_cart()

# 2. Adding the same product ID increases its quantity
print("\nADDING THE SAME PRODUCT AGAIN")
cart.add_to_cart(product2, 2)
cart.show_products_in_cart()

# 3. Update quantity using product ID
print("\nUPDATING QUANTITY")
cart.update_quantity(product3.product_id, 4)
cart.show_products_in_cart()

# 4. Remove part of a quantity using product ID
print("\nREMOVING PART OF A QUANTITY")
cart.remove_from_cart(product1.product_id, 1)
cart.show_products_in_cart()

# 5. Remove one specific product completely
print("\nREMOVING ONE MOUSE PRODUCT")
cart.remove_from_cart(product2.product_id)
cart.show_products_in_cart()

# The other Mouse product remains because its ID is different.
print("\nCHECKING THE OTHER MOUSE")
print(product4.product_details())
cart.show_products_in_cart()

# 6. Invalid operations should leave the cart unchanged
print("\nTESTING INVALID OPERATIONS")
previous_total = cart.total
previous_quantity = cart.total_quantity

try:
    cart.add_to_cart(product1, -2)
except (TypeError, ValueError) as error:
    print("Invalid addition:", error)

try:
    cart.update_quantity(product3.product_id, 0)
except (TypeError, ValueError) as error:
    print("Invalid update:", error)

try:
    cart.remove_from_cart(product1.product_id, 999)
except (TypeError, ValueError) as error:
    print("Invalid removal:", error)

print("Total unchanged:", cart.total == previous_total)
print("Quantity unchanged:", cart.total_quantity == previous_quantity)

# 7. Test invalid products
print("\nTESTING INVALID PRODUCTS")

try:
    Product("", 100)
except (TypeError, ValueError) as error:
    print("Invalid name:", error)

try:
    Product("Invalid Product", -100)
except (TypeError, ValueError) as error:
    print("Invalid price:", error)

# 8. Empty the cart
print("\nEMPTYING THE CART")
cart.remove_from_cart(product1.product_id)
cart.remove_from_cart(product3.product_id)
cart.remove_from_cart(product4.product_id)
cart.show_products_in_cart()

print("Final total:", cart.total)
