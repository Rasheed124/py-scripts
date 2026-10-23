from payments.payment_processor import PaymentProcessor


class CardPayment(PaymentProcessor):
    def __init__(self, should_succeed=True):
        self.should_succeed = bool(should_succeed)

    @property
    def method_name(self):
        return "card"

    def pay(self, amount):
        if amount < 0:
            raise ValueError("Payment amount cannot be negative.")
        print(f"[SIMULATED CARD] Attempting payment of ₦{amount:.2f}...")
        return self.should_succeed
