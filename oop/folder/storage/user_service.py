from typing import Any
from .base import Storage


class UserService:
    """Application service that depends on the Storage interface."""

    def __init__(self, storage: Storage) -> None:
        if not isinstance(storage, Storage):
            raise TypeError("storage must be an implementation of Storage.")
        self.storage = storage

    def save_user(self, user_id: str, user_data: dict[str, Any]) -> None:
        if not isinstance(user_data, dict):
            raise TypeError("user_data must be a dictionary.")
        self.storage.save(user_id, user_data)

    def get_user(self, user_id: str) -> dict[str, Any]:
        return self.storage.get(user_id)

    def delete_user(self, user_id: str) -> None:
        self.storage.delete(user_id)
