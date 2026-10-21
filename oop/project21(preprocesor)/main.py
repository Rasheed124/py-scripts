from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardProcessor(PaymentProcessor):

    CREDIT_CARD_FEE = 10

    def process_payment(self, amount):
        return amount * self.CREDIT_CARD_FEE
    


class BankTransferProcessor(PaymentProcessor):

    BANK_TRANSFER_CHARGES = 5

    def process_payment(self, amount):
        return amount * self.BANK_TRANSFER_CHARGES


class MobileWalletProcessor(PaymentProcessor):

    BANK_WALLET_REGULAR_CHARGES = 2

    def process_payment(self, amount):
        return amount * self.BANK_WALLET_REGULAR_CHARGES







# Create objects
credit_card = CreditCardProcessor()
bank_transfer = BankTransferProcessor()
mobile_wallet = MobileWalletProcessor()


# Store different processor objects in one list
payment_processors = [
    credit_card,
    bank_transfer,
    mobile_wallet,
]


# Test polymorphism
amount = 100

for processor in payment_processors:
    print(
        f"{type(processor).__name__}: "
        f"{processor.process_payment(amount)}"
    )


# Test creating an object without implementing process_payment()
class CashProcessor(PaymentProcessor):
    pass


cash = CashProcessor()