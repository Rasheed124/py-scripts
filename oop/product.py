
import random
import string

# name, price, and stock quantity.


# class Product:

    

#     def __init__(self, name, price, stock_quantity):

#         if not isinstance(price, (int, float)) or isinstance(price, bool):
#             raise TypeError("Price must be numeric.")

#         if not isinstance(stock_quantity, int) or isinstance(stock_quantity, bool):
#             raise TypeError("Stock quantity must be an integer.")

#         if price < 0:
#             raise ValueError("Price cannot be negative.")

#         if stock_quantity < 0:
#             raise ValueError("Stock quantity cannot be negative.")

#         self.name =  name
#         self.__price =  price
#         self.__stock_quantity =  stock_quantity
#         self.__product_id =  Product.generate_product_id()
#         self._product_list =  {}


#     def add_to_Stock(self):

#         if self.__product_id not in self._product_list:
#             self._product_list[self.__product_id] = {
#                 "name" : self.name ,
#                 "price" : self.__price, 
#                 "quantity" : self.__stock_quantity
#             }
#             print(f"Product - {self.name} added to stock successfully ")
#         else:
#             print(f"The product is in stock")


#     def remove_from_Stock(self):

#         if self.__product_id in self._product_list:
#             self._product_list.pop(self.__product_id )
#             print(f"Product Added to stock")
#         else:
#             print(f"The product not in stock")


#     def get_total_inventory(self):
#         total_inventory = {}

#         for product_id, details in self._product_list.items():
#             product_name = details['name']

#             for product_name in total_inventory:
#                 if product_name in total_inventory:
#                     total_inventory[product_name] += details['quantity']
#                 else:
#                     total_inventory[product_name] = details['price']

#         for key, value in total_inventory.items():
#             print(key, ":", value)


#     @staticmethod   
#     def generate_product_id():
#         return ''.join(
#             random.choices(string.ascii_uppercase + string.digits, k=8)
#         )



# bag1 = Product("Hand Bag", 3000, 3)
# bag2 = Product("Men Bag", 3000, 2)

# bag1.add_to_Stock()
# bag2.add_to_Stock()
# bag1.get_total_inventory()






class Product:
    _product_list = {}

    def __init__(self, name, price, stock_quantity):
        if not isinstance(price, (int, float)) or isinstance(price, bool):
            raise TypeError("Price must be numeric.")

        if not isinstance(stock_quantity, int) or isinstance(stock_quantity, bool):
            raise TypeError("Stock quantity must be an integer.")

        if price < 0:
            raise ValueError("Price cannot be negative.")

        if stock_quantity < 0:
            raise ValueError("Stock quantity cannot be negative.")

        self.name = name
        self.__price = price
        self.__stock_quantity = stock_quantity
        self.__product_id = self.generate_product_id()

    @property
    def price(self):
        return self.__price

    @property
    def stock_quantity(self):
        return self.__stock_quantity

    @property
    def product_id(self):
        return self.__product_id

    def add_stock(self, quantity):
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError("Quantity must be an integer.")

        if quantity <= 0:
            return "Quantity to add must be greater than zero."

        self.__stock_quantity += quantity

        if self.__product_id in Product._product_list:
            Product._product_list[self.__product_id]["quantity"] = (
                self.__stock_quantity
            )

        return f"Added {quantity} units of {self.name}."

    def remove_stock(self, quantity):
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError("Quantity must be an integer.")

        if quantity <= 0:
            return "Quantity to remove must be greater than zero."

        if quantity > self.__stock_quantity:
            return "Insufficient stock."

        self.__stock_quantity -= quantity

        if self.__product_id in Product._product_list:
            Product._product_list[self.__product_id]["quantity"] = (
                self.__stock_quantity
            )

        return f"Removed {quantity} units of {self.name}."

    def add_to_stock(self):
        if self.__product_id in Product._product_list:
            return f"{self.name} is already registered."

        Product._product_list[self.__product_id] = {
            "name": self.name,
            "price": self.__price,
            "quantity": self.__stock_quantity
        }

        return f"{self.name} added to inventory."

    def remove_from_stock(self):
        if self.__product_id not in Product._product_list:
            return f"{self.name} is not registered in inventory."

        del Product._product_list[self.__product_id]
        return f"{self.name} removed from inventory."

    def calculate_inventory_value(self):
        return self.__price * self.__stock_quantity

    def display_product_details(self):
        return (
            f"Product ID: {self.__product_id}\n"
            f"Product name: {self.name}\n"
            f"Price per unit: ₦{self.__price:,.2f}\n"
            f"Stock quantity: {self.__stock_quantity}\n"
            f"Inventory value: ₦{self.calculate_inventory_value():,.2f}"
        )

    @classmethod
    def get_total_inventory(cls):
        if not cls._product_list:
            print("The inventory is empty.")
            return

        total_quantity = 0
        total_value = 0

        print("\n--- Total Inventory ---")

        for product_id, details in cls._product_list.items():
            quantity = details["quantity"]
            value = details["price"] * quantity

            total_quantity += quantity
            total_value += value

            print(f"Product: {details['name']}")
            print(f"Product ID: {product_id}")
            print(f"Quantity: {quantity}")
            print(f"Value: ₦{value:,.2f}")
            print("-" * 25)

        print(f"Total units in stock: {total_quantity}")
        print(f"Total inventory value: ₦{total_value:,.2f}")

    @staticmethod
    def generate_product_id():
        import random
        import string

        while True:
            product_id = "".join(
                random.choices(
                    string.ascii_uppercase + string.digits,
                    k=8
                )
            )

            if product_id not in Product._product_list:
                return product_id


# Create three independent products
bag1 = Product("Hand Bag", 3000, 3)
bag2 = Product("Men Bag", 4500, 2)
bag3 = Product("School Bag", 2500, 5)

# Register products
print(bag1.add_to_stock())
print(bag2.add_to_stock())
print(bag3.add_to_stock())

# # Add and remove stock
print(bag1.add_stock(2))       # Hand Bag: 3 -> 5
print(bag2.remove_stock(1))    # Men Bag: 2 -> 1

# # Test invalid operations
print(bag1.remove_stock(100))  # Cannot remove more than available
print(bag3.add_stock(-2))      # Cannot add a negative quantity
print(bag3.remove_stock(0))    # Quantity must be positive

# # Display each product's details and individual value
print("\n--- Individual Product Details ---")
print(bag1.display_product_details())
print()
print(bag2.display_product_details())
print()
print(bag3.display_product_details())

# # Display the combined inventory
Product.get_total_inventory()

# # Check that products maintain independent stock
print("\n--- Independent Stock Check ---")
print("Hand Bag:", bag1.stock_quantity)       # 5
print("Men Bag:", bag2.stock_quantity)        # 1
print("School Bag:", bag3.stock_quantity)     # 5
