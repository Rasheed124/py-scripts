from typing import Any
from .base import Storage


class MemoryStorage(Storage):
    def __init__(self):
        self._data = {}

    def save_user(self, key: str, data: Any) -> None:
        self._data[key] = data

    def get_user(self, key: str) -> Any:
        return self._data.get(key)