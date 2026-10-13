
class Student:

    adult_age = 18

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def get_students_details(self):
        return f"{self.name} is {self.age} years old and studies {self.course}"

    def check_student_is_adult(self):
        return "You are an adult" if self.age >= Student.adult_age else "You are not an adult"


student1 = Student("Rasheed", 30, "Mathematics")
student1.name = "Habeeb"

student2 = Student("Adeola", 17, "Physics")

student3 = Student("Fatima", 20, "Computer Science")

# print(student1.get_students_details())
# print(student1.check_student_is_adult())

# print(student2.get_students_details())
# print(student2.check_student_is_adult())

# print(student3.get_students_details())
# print(student3.check_student_is_adult())

# # Demonstrate independent object state
# print("\nBefore changing student1's name:")
# print("Student 1:", student1.name)
# print("Student 2:", student2.name)

# student1.name = "Ibrahim"

# print("\nAfter changing student1's name:")
# print("Student 1:", student1.name)
# print("Student 2:", student2.name)



# ------------------------------------------------===== 2. Bank Account ==== ---------------------------------- #

# class BankAccount:

#     def __init__(self, account_holder, account_number, account_balance):
#         self.account_holder =  account_holder
#         self.__account_number = account_number  
#         self.__account_balance = account_balance


#     def deposit(self, account_number : str, amount : int):
#         if account_number == self.__account_number and amount > 0:
#             self.__account_balance += amount
#             return f"You've successfully deposited {amount} naira"
#         else:
#             return f"Oops your account number or amount is not valid, kindly try again"
        
        
#     def withdraw(self, account_number : str, amount : int):
#         if amount <= 0:
#             return "You can't withdrawal that amount"
#         elif account_number == self.__account_number and amount <= self.__account_balance:
#             self.__account_balance -= amount
#             return f"You've successfully withdrawal {amount} naira"
#         else:
#             return f"Oops your account number or amount is not valid, kindly try again"


#     def display_account_details(self):
#         return f"""Your account name is {self.account_holder} \nYour account number is {self.account_number} \nYour account balance is {self.account_balance}""".strip()

#     def check_balance(self):
#         return f"Your balance is {self.__account_balance}"


#     @property
#     def account_balance(self):
#         return self.__account_balance
    
#     @property
#     def account_number(self):
#         return self.__account_number

    

#     def __str__(self):
#         return f" This is {self.account_holder}'s account"



# banAccount1 = BankAccount('Rasheed', "2002100", 4000)
# banAccount2 = BankAccount('Adeola', "2002100", 4000)

# # print(banAccount2)

# print(banAccount1.display_account_details())
# print(banAccount1.deposit("2002100", 10))
# print(banAccount1.deposit("2002100", 10))
# print(banAccount1.check_balance())

# print(banAccount2.deposit("2002100", 70))
# print(banAccount2.deposit("2002100", 70))
# print(banAccount2.check_balance())



# AFTER AI REVIEW


class BankAccount:

    def __init__(self, account_holder, account_number, account_balance):
        if not isinstance(account_balance, (int, float)) or isinstance(account_balance, bool):
            raise TypeError("Account balance must be numeric.")

        if account_balance < 0:
            raise ValueError("Account balance cannot be negative.")

        self.account_holder = account_holder
        self.__account_number = str(account_number)
        self.__account_balance = account_balance

    def deposit(self, account_number: str, amount: int):
        if str(account_number) != self.__account_number:
            return "Invalid account number."

        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            return "Deposit amount must be numeric."

        if amount <= 0:
            return "Deposit amount must be greater than zero."

        self.__account_balance += amount
        return f"You have successfully deposited {amount} naira."

    def withdraw(self, account_number: str, amount: int):
        if str(account_number) != self.__account_number:
            return "Invalid account number."

        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            return "Withdrawal amount must be numeric."

        if amount <= 0:
            return "Withdrawal amount must be greater than zero."

        if amount > self.__account_balance:
            return "Insufficient funds."

        self.__account_balance -= amount
        return f"You have successfully withdrawn {amount} naira."

    def display_account_details(self):
        return (
            f"Account holder: {self.account_holder}\n"
            f"Account number: {self.account_number}\n"
            f"Account balance: {self.account_balance} naira"
        )

    def check_balance(self):
        return f"Your balance is {self.__account_balance} naira."

    @property
    def account_balance(self):
        return self.__account_balance

    @property
    def account_number(self):
        return self.__account_number

    def __str__(self):
        return f"This is {self.account_holder}'s account."


# banAccount1 = BankAccount("Rasheed", "2002100", 4000)
# banAccount2 = BankAccount("Adeola", "2002101", 4000)

# print(banAccount1.display_account_details())
# print(banAccount1.deposit("2002100", 10))
# print(banAccount1.withdraw("2002100", 500))
# print(banAccount1.withdraw("2002100", -100))
# print(banAccount1.withdraw("9999999", 100))
# print(banAccount1.check_balance())

# print("\nSecond account:")
# print(banAccount2.display_account_details())
# print(banAccount2.deposit("2002101", 70))
# print(banAccount2.check_balance())

# print("\nIndependent balance check:")
# print("Rasheed:", banAccount1.account_balance)
# print("Adeola:", banAccount2.account_balance)



import random
import string


class Product:

    # Shared inventory for all Product objects
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

bag1 = Product("Hand Bag", 3000, 3)
bag2 = Product("Men Bag", 3000, 2)

bag1.add_to_Stock()
bag2.add_to_Stock()
bag1.get_total_inventory()

    
        



