
# class DigitalWallet:
#     def __init__(
#         self,
#         owner_name: str,
#         owner_initial_balance: int | float,
#     ):
#         if (
#             not isinstance(owner_initial_balance, (int, float))
#             or isinstance(owner_initial_balance, bool)
#         ):
#             raise TypeError("Initial balance must be numeric.")

#         if owner_initial_balance < 0:
#             raise ValueError("Initial balance cannot be negative.")

#         if not isinstance(owner_name, str):
#             raise TypeError("Owner name must be a string.")

#         if not owner_name.strip():
#             raise ValueError("Owner name cannot be empty.")

#         self.__owner_name = owner_name.strip()
#         self.__balance = owner_initial_balance
#         self.__wallet_transaction_history = []

#     @property
#     def owner_name(self) -> str:
#         return self.__owner_name

#     @property
#     def balance(self) -> int | float:
#         return self.__balance

#     def _validate_amount(self, amount):
#         if (
#             not isinstance(amount, (int, float))
#             or isinstance(amount, bool)
#         ):
#             raise TypeError("Amount must be numeric.")

#         if amount <= 0:
#             raise ValueError("Amount must be greater than zero.")

#     def _record_transaction(self, transaction_type, amount):
#         self.__wallet_transaction_history.append({
#             "type": transaction_type,
#             "amount": amount,
#         })

#     def deposit(self, amount):
#         self._validate_amount(amount)

#         self.__balance += amount
#         self._record_transaction("deposit", amount)

#         print("Deposit made successfully and recorded.")

#     def make_payment(self, amount):
#         self._validate_amount(amount)

#         if amount > self.__balance:
#             raise ValueError("Insufficient funds.")

#         self.__balance -= amount
#         self._record_transaction("payment", amount)

#         print("Payment made successfully and recorded.")

#     def make_refund(self, amount):
#         self._validate_amount(amount)

#         self.__balance += amount
#         self._record_transaction("refund", amount)

#         print("Refund made successfully and recorded.")

#     def transaction_history(self):
#         print(f"\nTransaction history for {self.__owner_name}")
#         print("-" * 40)

#         if not self.__wallet_transaction_history:
#             print("No transactions recorded.")
#             return

#         total_deposit = 0
#         total_payment = 0
#         total_refund = 0

#         for index, transaction in enumerate(
#             self.__wallet_transaction_history, start=1
#         ):
#             transaction_type = transaction["type"]
#             amount = transaction["amount"]

#             print(
#                 f"{index}. {transaction_type.title()}: "
#                 f"{amount:.2f}"
#             )

#             if transaction_type == "deposit":
#                 total_deposit += amount
#             elif transaction_type == "payment":
#                 total_payment += amount
#             elif transaction_type == "refund":
#                 total_refund += amount

#         print("-" * 40)
#         print(f"Total deposits:  {total_deposit:.2f}")
#         print(f"Total payments:  {total_payment:.2f}")
#         print(f"Total refunds:   {total_refund:.2f}")
#         print(f"Current balance: {self.__balance:.2f}")


# user1 = DigitalWallet("ola", 400)

# user1.deposit(300)
# user1.deposit(200)
# user1.make_payment(100)
# user1.make_refund(50)

# print(f"\nBalance: {user1.balance:.2f}")

# user1.transaction_history()















from decimal import Decimal, InvalidOperation
from datetime import datetime, timezone
from uuid import uuid4


class DigitalWallet:
    def __init__(
        self,
        owner_name: str,
        owner_initial_balance: int | float | Decimal
    ):
        if not isinstance(owner_name, str):
            raise TypeError("Owner name must be a string.")

        if not owner_name.strip():
            raise ValueError("Owner name cannot be empty.")

        initial_balance = self._to_decimal(owner_initial_balance)

        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.__owner_name = owner_name.strip()
        self.__balance = initial_balance
        self.__wallet_transaction_history = []
        self.__payments = {}

    # ---------------- PROPERTIES ----------------

    @property
    def owner_name(self) -> str:
        return self.__owner_name

    @property
    def balance(self) -> Decimal:
        return self.__balance

    @property
    def transaction_history(self) -> tuple:
        return tuple(
            transaction.copy()
            for transaction in self.__wallet_transaction_history
        )

    # ---------------- VALIDATION ----------------

    @staticmethod
    def _to_decimal(amount) -> Decimal:
        if isinstance(amount, bool) or not isinstance(
            amount, (int, float, Decimal)
        ):
            raise TypeError("Amount must be a number.")

        try:
            value = Decimal(str(amount))
        except (InvalidOperation, ValueError):
            raise ValueError("Amount must be a valid number.")

        if not value.is_finite():
            raise ValueError("Amount must be finite.")

        return value

    @classmethod
    def _validate_amount(cls, amount) -> Decimal:
        value = cls._to_decimal(amount)

        if value <= 0:
            raise ValueError("Amount must be greater than zero.")

        return value

    # ---------------- TRANSACTIONS ----------------

    def _record_transaction(
        self,
        transaction_type: str,
        amount: Decimal,
        balance_after: Decimal,
        related_transaction_id: str | None = None
    ) -> str:
        transaction_id = f"TX-{uuid4().hex.upper()}"

        transaction = {
            "transaction_id": transaction_id,
            "type": transaction_type,
            "amount": amount,
            "balance_after": balance_after,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "related_transaction_id": related_transaction_id,
        }

        self.__wallet_transaction_history.append(transaction)

        return transaction_id

    def deposit(self, amount) -> str:
        amount = self._validate_amount(amount)

        new_balance = self.__balance + amount

        transaction_id = self._record_transaction(
            "deposit",
            amount,
            new_balance
        )

        self.__balance = new_balance

        print(f"Deposit successful. Transaction ID: {transaction_id}")
        return transaction_id

    def make_payment(self, amount) -> str:
        amount = self._validate_amount(amount)

        if amount > self.__balance:
            raise ValueError("Insufficient funds.")

        new_balance = self.__balance - amount

        transaction_id = self._record_transaction(
            "payment",
            amount,
            new_balance
        )

        self.__balance = new_balance

        # Track how much of this payment has been refunded.
        self.__payments[transaction_id] = {
            "amount": amount,
            "refunded": Decimal("0"),
        }

        print(f"Payment successful. Transaction ID: {transaction_id}")
        return transaction_id

    def make_refund(
        self,
        payment_transaction_id: str,
        amount
    ) -> str:
        amount = self._validate_amount(amount)

        payment = self.__payments.get(payment_transaction_id)

        if payment is None:
            raise ValueError(
                "Refund must reference a successful payment "
                "from this wallet."
            )

        remaining_refundable = payment["amount"] - payment["refunded"]

        if amount > remaining_refundable:
            raise ValueError(
                f"Refund exceeds the remaining refundable amount "
                f"of {remaining_refundable:.2f}."
            )

        new_balance = self.__balance + amount

        transaction_id = self._record_transaction(
            "refund",
            amount,
            new_balance,
            related_transaction_id=payment_transaction_id
        )

        self.__balance = new_balance
        payment["refunded"] += amount

        print(f"Refund successful. Transaction ID: {transaction_id}")
        return transaction_id

    # ---------------- BALANCE CHECK ----------------

    def check_balance(self) -> Decimal:
        print(f"Current balance: {self.__balance:.2f}")
        return self.__balance

    # ---------------- HISTORY DISPLAY ----------------

    def display_transaction_history(self):
        print(f"\nTransaction history for {self.__owner_name}")
        print("-" * 70)

        if not self.__wallet_transaction_history:
            print("No transactions recorded.")
            return

        total_deposits = Decimal("0")
        total_payments = Decimal("0")
        total_refunds = Decimal("0")

        for index, transaction in enumerate(
            self.__wallet_transaction_history,
            start=1
        ):
            transaction_type = transaction["type"]
            amount = transaction["amount"]

            print(f"{index}. ID: {transaction['transaction_id']}")
            print(f"   Type: {transaction_type.title()}")
            print(f"   Amount: {amount:.2f}")
            print(
                f"   Balance after: "
                f"{transaction['balance_after']:.2f}"
            )
            print(f"   Timestamp: {transaction['timestamp']}")

            related_id = transaction["related_transaction_id"]
            if related_id:
                print(f"   Related payment: {related_id}")

            print("-" * 70)

            if transaction_type == "deposit":
                total_deposits += amount
            elif transaction_type == "payment":
                total_payments += amount
            elif transaction_type == "refund":
                total_refunds += amount

        print(f"Total deposits:  {total_deposits:.2f}")
        print(f"Total payments:  {total_payments:.2f}")
        print(f"Total refunds:   {total_refunds:.2f}")
        print(f"Current balance: {self.__balance:.2f}")


# ==================== TESTING ====================

wallet = DigitalWallet("Ola", Decimal("400.00"))

# 1. Successful deposits
wallet.deposit(Decimal("300.00"))
wallet.deposit(Decimal("200.00"))

# 2. Successful payment: save its ID so it can be refunded
payment_id = wallet.make_payment(Decimal("100.00"))

# 3. Successful partial refund
wallet.make_refund(payment_id, Decimal("30.00"))

# 4. Another partial refund of the same payment
wallet.make_refund(payment_id, Decimal("20.00"))

wallet.check_balance()
wallet.display_transaction_history()

# 5. Invalid transactions must not change the balance or history
print("\nTESTING INVALID TRANSACTIONS")

def test_invalid_transaction(description, operation):
    previous_balance = wallet.balance
    previous_history = wallet.transaction_history

    try:
        operation()
    except (TypeError, ValueError) as error:
        print(f"{description}: rejected ({error})")
    else:
        print(f"{description}: unexpectedly succeeded")

    print("Balance unchanged:", wallet.balance == previous_balance)
    print("History unchanged:", wallet.transaction_history == previous_history)


test_invalid_transaction(
    "Negative deposit",
    lambda: wallet.deposit(-50)
)

test_invalid_transaction(
    "Zero payment",
    lambda: wallet.make_payment(0)
)

test_invalid_transaction(
    "Boolean deposit",
    lambda: wallet.deposit(True)
)

test_invalid_transaction(
    "NaN deposit",
    lambda: wallet.deposit(float("nan"))
)

test_invalid_transaction(
    "Infinite payment",
    lambda: wallet.make_payment(float("inf"))
)

test_invalid_transaction(
    "Payment exceeding balance",
    lambda: wallet.make_payment(100000)
)

test_invalid_transaction(
    "Refund exceeding remaining refundable amount",
    lambda: wallet.make_refund(payment_id, 100)
)

test_invalid_transaction(
    "Refund for unknown payment",
    lambda: wallet.make_refund("INVALID-ID", 10)
)

# 6. Test transaction-history protection
print("\nTESTING HISTORY PROTECTION")

history_snapshot = wallet.transaction_history

try:
    history_snapshot[0]["amount"] = Decimal("999999")
except (TypeError, AttributeError) as error:
    print("History snapshot is immutable:", error)

print("Wallet history amount:", wallet.transaction_history[0]["amount"])
print("Wallet balance:", wallet.balance)
