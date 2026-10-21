from decimal import Decimal
from .customer import Customer
from .validators import to_decimal, validate_name

class BusinessCustomer(Customer):
    """Business customer with registration details and bulk discounts."""
    DISCOUNT_THRESHOLD = Decimal("10000")
    DISCOUNT_RATE = Decimal("0.15")

    def __init__(self, user_name: str, email: str, business_name: str, registration_number: str):
        super().__init__(user_name, email)
        self.__business_name = validate_name(business_name, "Business name")
        self.__registration_number = validate_name(registration_number, "Registration number")

    @property
    def customer_type(self) -> str:
        return "Business"

    @property
    def business_name(self) -> str:
        return self.__business_name

    @property
    def registration_number(self) -> str:
        return self.__registration_number

    def cal_discount(self, subtotal: Decimal) -> Decimal:
        subtotal = to_decimal(subtotal)
        return subtotal * self.DISCOUNT_RATE if subtotal >= self.DISCOUNT_THRESHOLD else Decimal("0")

    def display_user_information(self) -> str:
        return (f"{super().display_user_information()}\n"
                f"Business name: {self.business_name}\n"
                f"Registration number: {self.registration_number}\n"
                "Business benefit: 15% discount on purchases of ₦10,000 or more")
