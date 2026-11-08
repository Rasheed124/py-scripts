from decimal import Decimal, InvalidOperation


def validate_currency(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("Currency must be a string.")

    currency = value.strip().upper()
    if not currency:
        raise ValueError("Currency cannot be empty.")

    if len(currency) != 3 or not currency.isalpha():
        raise ValueError("Currency must be a three-letter code, such as NGN or USD.")

    return currency


def to_decimal(value) -> Decimal:
    if isinstance(value, bool):
        raise TypeError("Amount cannot be a boolean.")

    if not isinstance(value, (int, float, str, Decimal)):
        raise TypeError("Amount must be an int, float, string, or Decimal.")

    try:
        amount = Decimal(str(value).strip())
    except (InvalidOperation, ValueError):
        raise ValueError("Amount must be a valid numeric value.") from None

    if not amount.is_finite():
        raise ValueError("Amount must be finite.")

    return amount
