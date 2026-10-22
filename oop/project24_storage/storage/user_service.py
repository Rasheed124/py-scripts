from typing import Any
from .base import Storage


class UserService:
    def __init__(self, storage: Storage):
        self.storage = storage

    def save_user(self, user_id: str, user_data: dict) -> None:
        self.storage.save(user_id, user_data)

    def get_user(self, user_id: str) -> Any:
        return self.storage.get(user_id)