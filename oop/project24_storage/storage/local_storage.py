from typing import Any
from .base import Storage


class LocalStorage(Storage):
    def save_user(self, key: str, data: Any) -> None:
        # Implement file-based saving
        pass

    def get_user(self, key: str) -> Any:
        # Implement file-based retrieval
        pass