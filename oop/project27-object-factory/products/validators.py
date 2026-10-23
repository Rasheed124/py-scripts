from decimal import Decimal, InvalidOperation


def validate_name(value: str, field_name: str = "Name") -> str:
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string.")
    value = value.strip()
    if not value:
        raise ValueError(f"{field_name} cannot be empty.")
    return value


def to_decimal(value) -> Decimal:
    if isinstance(value, bool) or not isinstance(value, (int, float, Decimal, str)):
        raise TypeError("Price must be an int, float, Decimal, or numeric string.")
    try:
        result = Decimal(str(value).strip())
    except (InvalidOperation, ValueError):
        raise ValueError("Price must be a valid number.") from None
    if not result.is_finite():
        raise ValueError("Price must be finite.")
    return result


def validate_positive_price(value) -> Decimal:
    price = to_decimal(value)
    if price <= 0:
        raise ValueError("Price must be greater than zero.")
    return price


def validate_quantity(value) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("Quantity must be an integer.")
    if value <= 0:
        raise ValueError("Quantity must be greater than zero.")
    return value


def validate_non_negative_int(value, field_name: str = "Value") -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{field_name} must be an integer.")
    if value < 0:
        raise ValueError(f"{field_name} cannot be negative.")
    return value
