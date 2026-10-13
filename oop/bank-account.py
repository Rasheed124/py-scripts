# ------------------------------------------------===== 2. Bank Account ==== ---------------------------------- #

class BankAccount:

    def __init__(self, account_holder, account_number, account_balance):
        self.account_holder =  account_holder
        self.__account_number = account_number  
        self.__account_balance = account_balance


    def deposit(self, account_number : str, amount : int):
        if account_number == self.__account_number and amount > 0:
            self.__account_balance += amount
            return f"You've successfully deposited {amount} naira"
        else:
            return f"Oops your account number or amount is not valid, kindly try again"
        
        
    def withdraw(self, account_number : str, amount : int):
        if amount <= 0:
            return "You can't withdrawal that amount"
        elif account_number == self.__account_number and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"You've successfully withdrawal {amount} naira"
        else:
            return f"Oops your account number or amount is not valid, kindly try again"


    def display_account_details(self):
        return f"""Your account name is {self.account_holder} \nYour account number is {self.account_number} \nYour account balance is {self.account_balance}""".strip()

    def check_balance(self):
        return f"Your balance is {self.__account_balance}"


    @property
    def account_balance(self):
        return self.__account_balance
    
    @property
    def account_number(self):
        return self.__account_number

    

    def __str__(self):
        return f" This is {self.account_holder}'s account"



banAccount1 = BankAccount('Rasheed', "2002100", 4000)
banAccount2 = BankAccount('Adeola', "2002100", 4000)

# print(banAccount2)

print(banAccount1.display_account_details())
print(banAccount1.deposit("2002100", 10))
print(banAccount1.deposit("2002100", 10))
print(banAccount1.check_balance())

print(banAccount2.deposit("2002100", 70))
print(banAccount2.deposit("2002100", 70))
print(banAccount2.check_balance())



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
