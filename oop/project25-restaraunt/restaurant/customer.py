from .validators import validate_name

class Customer:
    """Stores customer details."""
    def __init__(self, customer_id: str, name: str, email: str):
        self.__customer_id = validate_name(customer_id, "Customer ID")
        self.__name = validate_name(name, "Customer name")
        self.__email = validate_name(email, "Email")
        if "@" not in self.__email or "." not in self.__email.rsplit("@", 1)[-1]:
            raise ValueError("Email address does not appear to be valid.")

    @property
    def customer_id(self) -> str:
        return self.__customer_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email

    def __str__(self) -> str:
        return f"{self.name} ({self.customer_id})"
