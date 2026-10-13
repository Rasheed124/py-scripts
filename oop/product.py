
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





# import random
# import string


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
        self.__product_id = Product.generate_product_id()

    def add_to_Stock(self):

        if self.__product_id not in Product._product_list:
            Product._product_list[self.__product_id] = {
                "name": self.name,
                "price": self.__price,
                "quantity": self.__stock_quantity
            }

            print(f"Product - {self.name} added to stock successfully.")

        else:
            print("The product is already in stock.")

    def remove_from_Stock(self):

        if self.__product_id in Product._product_list:
            Product._product_list.pop(self.__product_id)
            print(f"Product - {self.name} removed from stock.")

        else:
            print("The product is not in stock.")

    @classmethod
    def get_total_inventory(cls):

        total_inventory = {}

        for product_id, details in cls._product_list.items():

            product_name = details["name"]
            quantity = details["quantity"]
            value = details["price"] * quantity

            if product_name in total_inventory:
                total_inventory[product_name]["quantity"] += quantity
                total_inventory[product_name]["value"] += value

            else:
                total_inventory[product_name] = {
                    "quantity": quantity,
                    "value": value
                }

        print("\n--- Total Inventory ---")

        if not total_inventory:
            print("The inventory is empty.")
            return

        for name, details in total_inventory.items():
            print(f"Product: {name}")
            print(f"Total quantity: {details['quantity']}")
            print(f"Total value: ₦{details['value']:,.2f}")
            print("-" * 25)

        total_quantity = sum(
            details["quantity"]
            for details in total_inventory.values()
        )

        total_value = sum(
            details["value"]
            for details in total_inventory.values()
        )

        print(f"Total items in stock: {total_quantity}")
        print(f"Total inventory value: ₦{total_value:,.2f}")


    @staticmethod
    def generate_product_id():

        while True:
            product_id = ''.join(
                random.choices(
                    string.ascii_uppercase + string.digits,
                    k=8
                )
            )

            if product_id not in Product._product_list:
                return product_id



# bag1 = Product("Hand Bag", 3000, 3)
# bag2 = Product("Men Bag", 3000, 2)

# bag1.add_to_Stock()
# bag2.add_to_Stock()
# bag1.get_total_inventory()

