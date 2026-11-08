from decimal import Decimal

from .validators import to_decimal, validate_currency


class Money:
    """Represent a monetary amount in a specific currency."""

    def __init__(self, amount, currency: str):
        self.__amount = to_decimal(amount)
        self.__currency = validate_currency(currency)

    @property
    def amount(self) -> Decimal:
        return self.__amount

    @property
    def currency(self) -> str:
        return self.__currency

    def __str__(self) -> str:
        return f"{self.currency} {self.amount:,.2f}"

    def __repr__(self) -> str:
        return (
            f"Money(amount=Decimal('{self.amount}'), "
            f"currency={self.currency!r})"
        )

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._ensure_compatible_currency(other)
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._ensure_compatible_currency(other)
        return Money(self.amount - other.amount, self.currency)

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other):
        self._ensure_money(other)
        self._ensure_compatible_currency(other)
        return self.amount < other.amount

    def __le__(self, other):
        self._ensure_money(other)
        self._ensure_compatible_currency(other)
        return self.amount <= other.amount

    def __gt__(self, other):
        self._ensure_money(other)
        self._ensure_compatible_currency(other)
        return self.amount > other.amount

    def __ge__(self, other):
        self._ensure_money(other)
        self._ensure_compatible_currency(other)
        return self.amount >= other.amount

    def _ensure_money(self, other) -> None:
        if not isinstance(other, Money):
            raise TypeError("Money can only be compared with another Money object.")

    def _ensure_compatible_currency(self, other) -> None:
        self._ensure_money(other)
        if self.currency != other.currency:
            raise ValueError(
                f"Cannot operate on different currencies: "
                f"{self.currency} and {other.currency}."
            )
