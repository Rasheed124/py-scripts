# from decimal import Decimal, InvalidOperation
# from uuid import uuid4


# class PaymentMethod:
#     payments_history = []

#     def __init__(
#         self,
#         payment_method_name: str,
#         payment_method_amount: int | float | Decimal,
#     ):
#         if not isinstance(payment_method_name, str):
#             raise TypeError("Payment method name must be a string.")

#         if not payment_method_name.strip():
#             raise ValueError("Payment method name cannot be empty.")

#         self.__payment_method_name = payment_method_name.strip()
#         self.__payment_method_amount = self._validate_amount(
#             payment_method_amount
#         )

#     # ---------------- PROPERTIES ----------------

#     @property
#     def payment_method_name(self) -> str:
#         return self.__payment_method_name

#     @property
#     def payment_method_amount(self) -> Decimal:
#         return self.__payment_method_amount

#     # ---------------- TRANSACTIONS ----------------

#     def _record_payment_transaction(
#         self,
#         transaction_type: str,
#         amount: Decimal,
#     ) -> str:
#         transaction_id = f"TX-{uuid4().hex.upper()}"

#         transaction = {
#             "transaction_id": transaction_id,
#             "type": transaction_type,
#             "payment_method": self.payment_method_name,
#             "amount": amount,
#         }

#         PaymentMethod.payments_history.append(transaction)

#         return transaction_id

#     # ---------------- VALIDATION ----------------

#     @staticmethod
#     def _to_decimal(amount) -> Decimal:
#         if isinstance(amount, bool) or not isinstance(
#             amount, (int, float, Decimal)
#         ):
#             raise TypeError("Amount must be a number.")

#         try:
#             value = Decimal(str(amount))
#         except (InvalidOperation, ValueError):
#             raise ValueError("Amount must be a valid number.") from None

#         if not value.is_finite():
#             raise ValueError("Amount must be finite.")

#         return value

#     @classmethod
#     def _validate_amount(cls, amount) -> Decimal:
#         value = cls._to_decimal(amount)

#         if value <= 0:
#             raise ValueError("Amount must be greater than zero.")

#         return value

#     # ---------------- PAYMENT METHODS ----------------

#     def process_payment(self) -> Decimal:
#         return self.payment_method_amount

#     def checkout(self) -> str:
#         amount = self.process_payment()

#         return self._record_payment_transaction(
#             self.transaction_type,
#             amount,
#         )


# class CreditCardPayment(PaymentMethod):
#     transaction_type = "credit_card"

#     def initialize_credit_card_payment(self) -> str:
#         return self.checkout()


# class BankTransferPayment(PaymentMethod):
#     transaction_type = "bank_transfer"

#     def initialize_bank_transfer_payment(self) -> str:
#         return self.checkout()


# class MobileWalletPayment(PaymentMethod):
#     transaction_type = "mobile_wallet"

#     def initialize_mobile_wallet_payment(self) -> str:
#         return self.checkout()














from decimal import Decimal, InvalidOperation
from uuid import uuid4
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    payments_history = []

    def __init__(self, payment_method_name: str):
        if not isinstance(payment_method_name, str):
            raise TypeError("Payment method name must be a string.")

        if not payment_method_name.strip():
            raise ValueError("Payment method name cannot be empty.")

        self.__payment_method_name = payment_method_name.strip()

    @property
    def payment_method_name(self) -> str:
        return self.__payment_method_name

    # ---------- AMOUNT VALIDATION ----------

    @staticmethod
    def _to_decimal(amount) -> Decimal:
        if isinstance(amount, bool) or not isinstance(
            amount, (int, float, Decimal)
        ):
            raise TypeError("Amount must be a number.")

        try:
            value = Decimal(str(amount))
        except (InvalidOperation, ValueError):
            raise ValueError("Amount must be a valid number.") from None

        if not value.is_finite():
            raise ValueError("Amount must be finite.")

        return value

    @classmethod
    def validate_amount(cls, amount) -> Decimal:
        value = cls._to_decimal(amount)

        if value <= 0:
            raise ValueError("Payment amount must be greater than zero.")

        return value

    # ---------- SHARED PAYMENT INTERFACE ----------

    @abstractmethod
    def process_payment(self, amount: Decimal) -> dict:
        """Each subclass implements its own payment behavior."""
        pass

    # ---------- TRANSACTION HISTORY ----------

    @classmethod
    def _record_transaction(
        cls,
        payment_method: str,
        amount: Decimal,
        status: str,
        message: str,
    ) -> dict:
        transaction = {
            "transaction_id": f"TX-{uuid4().hex[:12].upper()}",
            "payment_method": payment_method,
            "amount": amount,
            "status": status,
            "message": message,
        }

        PaymentMethod.payments_history.append(transaction.copy())
        return transaction

    @classmethod
    def get_transaction_history(cls) -> tuple:
        return tuple(
            transaction.copy()
            for transaction in PaymentMethod.payments_history
        )


# ==================================================
# CREDIT CARD PAYMENT
# ==================================================

class CreditCardPayment(PaymentMethod):
    def __init__(self, card_holder: str):
        super().__init__("Credit Card")

        if not isinstance(card_holder, str):
            raise TypeError("Card holder must be a string.")

        if not card_holder.strip():
            raise ValueError("Card holder cannot be empty.")

        self.__card_holder = card_holder.strip()

    def process_payment(self, amount: Decimal) -> dict:
        amount = self.validate_amount(amount)

        return self._record_transaction(
            self.payment_method_name,
            amount,
            "successful",
            f"Card payment approved for {self.__card_holder}.",
        )


# ==================================================
# BANK TRANSFER PAYMENT
# ==================================================

class BankTransferPayment(PaymentMethod):
    def __init__(self, account_name: str):
        super().__init__("Bank Transfer")

        if not isinstance(account_name, str):
            raise TypeError("Account name must be a string.")

        if not account_name.strip():
            raise ValueError("Account name cannot be empty.")

        self.__account_name = account_name.strip()

    def process_payment(self, amount: Decimal) -> dict:
        amount = self.validate_amount(amount)

        # Simulate generating a bank transfer reference.
        transfer_reference = f"BT-{uuid4().hex[:10].upper()}"

        result = self._record_transaction(
            self.payment_method_name,
            amount,
            "successful",
            f"Transfer initiated for {self.__account_name}.",
        )

        result["transfer_reference"] = transfer_reference
        PaymentMethod.payments_history[-1]["transfer_reference"] = (
            transfer_reference
        )

        return result


# ==================================================
# MOBILE WALLET PAYMENT
# ==================================================

class MobileWalletPayment(PaymentMethod):
    def __init__(self, wallet_number: str):
        super().__init__("Mobile Wallet")

        if not isinstance(wallet_number, str):
            raise TypeError("Wallet number must be a string.")

        if not wallet_number.strip():
            raise ValueError("Wallet number cannot be empty.")

        self.__wallet_number = wallet_number.strip()

    def process_payment(self, amount: Decimal) -> dict:
        amount = self.validate_amount(amount)

        # Simulate mobile wallet confirmation.
        return self._record_transaction(
            self.payment_method_name,
            amount,
            "successful",
            f"Wallet payment confirmed for {self.__wallet_number}.",
        )


# ==================================================
# FOURTH PAYMENT TYPE: GIFT CARD
# ==================================================

class GiftCardPayment(PaymentMethod):
    def __init__(self, gift_card_code: str):
        super().__init__("Gift Card")

        if not isinstance(gift_card_code, str):
            raise TypeError("Gift card code must be a string.")

        if not gift_card_code.strip():
            raise ValueError("Gift card code cannot be empty.")

        self.__gift_card_code = gift_card_code.strip()

    def process_payment(self, amount: Decimal) -> dict:
        amount = self.validate_amount(amount)

        # Simulate gift card payment.
        return self._record_transaction(
            self.payment_method_name,
            amount,
            "successful",
            f"Gift card {self.__gift_card_code} accepted.",
        )


# ==================================================
# SHARED CHECKOUT WORKFLOW
# ==================================================

def checkout(payment_method: PaymentMethod, amount) -> dict:
    if not isinstance(payment_method, PaymentMethod):
        raise TypeError("A valid PaymentMethod object is required.")

    validated_amount = PaymentMethod.validate_amount(amount)

    result = payment_method.process_payment(validated_amount)

    print("\n========== CHECKOUT RESULT ==========")
    print(f"Transaction ID: {result['transaction_id']}")
    print(f"Payment Method:  {result['payment_method']}")
    print(f"Amount:          ₦{result['amount']:,.2f}")
    print(f"Status:          {result['status'].upper()}")
    print(f"Message:         {result['message']}")
    print("=====================================")

    return result


# ==================================================
# TESTING
# ==================================================

if __name__ == "__main__":

    credit_card = CreditCardPayment("John Doe")
    bank_transfer = BankTransferPayment("John Doe")
    mobile_wallet = MobileWalletPayment("08012345678")
    gift_card = GiftCardPayment("GIFT-2026-ABC")

    # All payment methods use the same checkout function.
    payment_methods = [
        credit_card,
        bank_transfer,
        mobile_wallet,
        gift_card,
    ]

    print("\nTEST 1: PROCESS PAYMENTS")

    for method in payment_methods:
        checkout(method, 25000)

    # Test invalid amounts.
    print("\nTEST 2: INVALID PAYMENT AMOUNTS")

    invalid_amounts = [
        0,
        -500,
        True,
        "1000",
        None,
        float("inf"),
        float("nan"),
    ]

    for invalid_amount in invalid_amounts:
        try:
            checkout(credit_card, invalid_amount)
        except (TypeError, ValueError) as error:
            print(
                f"Rejected {invalid_amount!r}: {error}"
            )

    # Show that all transactions were recorded.
    print("\nTEST 3: TRANSACTION HISTORY")

    for transaction in PaymentMethod.get_transaction_history():
        print(transaction)

    print(
        "\nTotal recorded transactions:",
        len(PaymentMethod.get_transaction_history()),
    )
