from decimal import Decimal, InvalidOperation


def validate_non_empty_string(value, field_name="value"):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string.")
    return value.strip()


def validate_email(value):
    value = validate_non_empty_string(value, "Email")
    if "@" not in value or "." not in value.rsplit("@", 1)[-1]:
        raise ValueError("Enter a valid email address.")
    return value


def validate_phone(value):
    value = validate_non_empty_string(value, "Phone")
    if len(value) < 7:
        raise ValueError("Phone number must contain at least 7 characters.")
    return value


def validate_positive_quantity(value):
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("Quantity must be a positive integer.")
    return value


def validate_price(value):
    try:
        amount = Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError):
        raise ValueError("Price must be a valid number.") from None
    if not amount.is_finite() or amount < 0:
        raise ValueError("Price must be a finite, non-negative amount.")
    return amount.quantize(Decimal("0.01"))


def validate_stock(value):
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError("Stock must be a non-negative integer.")
    return value
