from decimal import Decimal
from .customer import Customer
from .validators import to_decimal

class PremiumCustomer(Customer):
    """Premium customer with membership benefits."""
    DISCOUNT_RATE = Decimal("0.10")

    def __init__(self, user_name: str, email: str):
        super().__init__(user_name, email)
        self.__membership_level = "Gold"

    @property
    def customer_type(self) -> str:
        return "Premium"

    @property
    def membership_level(self) -> str:
        return self.__membership_level

    def cal_discount(self, subtotal: Decimal) -> Decimal:
        subtotal = to_decimal(subtotal)
        return subtotal * self.DISCOUNT_RATE if subtotal > 0 else Decimal("0")

    def display_user_information(self) -> str:
        return (f"{super().display_user_information()}\n"
                f"Membership level: {self.membership_level}\n"
                "Premium benefit: 10% discount on eligible purchases")
