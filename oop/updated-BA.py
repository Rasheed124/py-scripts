
class BankAccount:

    def __init__(
        self,
        account_holder: str,
        account_number: str,
        account_balance: int | float
    ):
        if not isinstance(account_holder, str):
            raise TypeError("Account holder must be a string.")

        if not account_holder.strip():
            raise ValueError("Account holder cannot be empty.")

        if not isinstance(account_number, str):
            raise TypeError("Account number must be a string.")

        if not account_number.strip():
            raise ValueError("Account number cannot be empty.")

        if (
            not isinstance(account_balance, (int, float))
            or isinstance(account_balance, bool)
        ):
            raise TypeError("Account balance must be numeric.")

        if account_balance < 0:
            raise ValueError("Account balance cannot be negative.")

        self.__account_holder = account_holder.strip()
        self.__account_number = account_number.strip()
        self.__account_balance = account_balance

    # Read-only properties

    @property
    def account_holder(self) -> str:
        return self.__account_holder

    @property
    def account_number(self) -> str:
        return self.__account_number

    @property
    def account_balance(self) -> int | float:
        return self.__account_balance

    # Transaction methods

    def deposit(self, account_number: str, amount: int | float) -> str:
        if str(account_number) != self.__account_number:
            return "Invalid account number."

        if (
            not isinstance(amount, (int, float))
            or isinstance(amount, bool)
        ):
            return "Deposit amount must be numeric."

        if amount <= 0:
            return "Deposit amount must be greater than zero."

        self.__account_balance += amount

        return f"Successfully deposited {amount} naira."

    def withdraw(self, account_number: str, amount: int | float) -> str:
        if str(account_number) != self.__account_number:
            return "Invalid account number."

        if (
            not isinstance(amount, (int, float))
            or isinstance(amount, bool)
        ):
            return "Withdrawal amount must be numeric."

        if amount <= 0:
            return "Withdrawal amount must be greater than zero."

        if amount > self.__account_balance:
            return "Insufficient funds."

        self.__account_balance -= amount

        return f"Successfully withdrawn {amount} naira."

    # Display methods

    def check_balance(self) -> str:
        return f"Your balance is {self.__account_balance} naira."

    def display_account_details(self) -> str:
        return (
            f"Account holder: {self.account_holder}\n"
            f"Account number: {self.account_number}\n"
            f"Account balance: {self.account_balance} naira"
        )

    def __str__(self) -> str:
        return f"This is {self.account_holder}'s account."


# ==========================================
# 1. Create independent accounts
# ==========================================

account1 = BankAccount("Rasheed", "2002100", 4000)
account2 = BankAccount("Adeola", "2002101", 2500)

print(account1.display_account_details())
print()
print(account2.display_account_details())


# ==========================================
# 2. Test successful transactions
# ==========================================

print("\n--- Successful Transactions ---")

print(account1.deposit("2002100", 1000))
print(account1.withdraw("2002100", 500))
print(account1.check_balance())  # 4500


# ==========================================
# 3. Test invalid transactions
# ==========================================

print("\n--- Invalid Transactions ---")

print(account1.deposit("2002100", 0))
print(account1.deposit("2002100", -500))
print(account1.deposit("2002100", "hello"))
print(account1.deposit("2002100", True))

print(account1.withdraw("2002100", 0))
print(account1.withdraw("2002100", -500))
print(account1.withdraw("2002100", "hello"))
print(account1.withdraw("2002100", True))
print(account1.withdraw("2002100", 100000))
print(account1.withdraw("wrong-number", 100))


# ==========================================
# 4. Confirm failed transactions preserve state
# ==========================================

print("\n--- Transaction Integrity ---")

balance_before = account1.account_balance

account1.withdraw("2002100", 100000)

balance_after = account1.account_balance

print("Balance before:", balance_before)
print("Balance after:", balance_after)
print("Balance unchanged:", balance_before == balance_after)


# ==========================================
# 5. Test independent account balances
# ==========================================

print("\n--- Independent Accounts ---")

print("Account 1:", account1.account_balance)
print("Account 2:", account2.account_balance)

account1.deposit("2002100", 500)

print("Account 1 after deposit:", account1.account_balance)
print("Account 2 remains unchanged:", account2.account_balance)


# ==========================================
# 6. Test public property protection
# ==========================================

print("\n--- Public Property Protection ---")

balance_before = account1.account_balance

try:
    account1.account_balance = -5000
except AttributeError as error:
    print("Assignment rejected:", error)

print("Balance unchanged:", account1.account_balance == balance_before)


# ==========================================
# 7. Demonstrate name mangling
# ==========================================

print("\n--- Name Mangling Demonstration ---")

account1.__account_balance = 1000

# This creates a separate attribute; it does not change
# the balance exposed by the property.
print("Balance through property:", account1.account_balance)
print("Extra attribute:", account1.__account_balance)

# WARNING: This deliberately changes the actual internal balance.
# It demonstrates why name mangling is not a security boundary.
# Do not use this technique in normal application code.
account1._BankAccount__account_balance = 4500

print("Balance after deliberate internal access:", account1.account_balance)


# ==========================================
# 8. Test invalid constructor arguments
# ==========================================

print("\n--- Constructor Validation ---")

invalid_accounts = [
    ("Empty holder", "", "2003000", 1000),
    ("Whitespace holder", "   ", "2003001", 1000),
    ("Non-string holder", 123, "2003002", 1000),
    ("Empty account number", "John", "   ", 1000),
    ("Negative balance", "John", "2003003", -100),
    ("String balance", "John", "2003004", "1000"),
    ("Boolean balance", "John", "2003005", True),
]

for description, holder, number, balance in invalid_accounts:
    try:
        BankAccount(holder, number, balance)
    except (TypeError, ValueError) as error:
        print(f"{description}: {type(error).__name__}: {error}")
