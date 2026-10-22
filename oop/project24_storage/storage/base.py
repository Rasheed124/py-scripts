from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def save_user(self, key: str, data: bytes) -> None:
        """Save data under the given key."""
        pass

    @abstractmethod
    def get_user(self, key: str) -> bytes:
        """Load data associated with the given key."""
        pass