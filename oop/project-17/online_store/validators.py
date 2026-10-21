from decimal import Decimal, InvalidOperation

def validate_name(value: str, field_name: str = "Name") -> str:
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string.")
    value = value.strip()
    if not value:
        raise ValueError(f"{field_name} cannot be empty.")
    return value

def validate_email(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("Email must be a string.")
    value = value.strip()
    if (not value or value.count("@") != 1 or value.startswith("@")
        or value.endswith("@") or any(c.isspace() for c in value)
        or "." not in value.split("@")[1] or value.endswith(".")):
        raise ValueError("Please provide a valid email address.")
    return value

def to_decimal(value) -> Decimal:
    if isinstance(value, bool) or not isinstance(value, (int, float, Decimal)):
        raise TypeError("Amount must be an int, float, or Decimal.")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise ValueError("Amount must be a valid number.") from None
    if not result.is_finite():
        raise ValueError("Amount must be finite.")
    return result

def validate_positive_amount(value) -> Decimal:
    amount = to_decimal(value)
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    return amount

def validate_quantity(quantity: int) -> int:
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError("Quantity must be an integer.")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    return quantity
