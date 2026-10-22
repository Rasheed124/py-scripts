from typing import Any
from .base import Storage


class MemoryStorage(Storage):
    """Store records in a dictionary for the lifetime of the process."""

    def __init__(self) -> None:
        self._data: dict[str, Any] = {}

    @staticmethod
    def _validate_key(key: str) -> None:
        if not isinstance(key, str):
            raise TypeError("Storage key must be a string.")
        if not key.strip():
            raise ValueError("Storage key cannot be empty.")

    def save(self, key: str, data: Any) -> None:
        self._validate_key(key)
        self._data[key] = data

    def get(self, key: str) -> Any:
        self._validate_key(key)
        try:
            return self._data[key]
        except KeyError:
            raise KeyError(f"No record found for key: {key!r}") from None

    def delete(self, key: str) -> None:
        self._validate_key(key)
        try:
            del self._data[key]
        except KeyError:
            raise KeyError(f"No record found for key: {key!r}") from None
