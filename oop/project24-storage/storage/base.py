from abc import ABC, abstractmethod
from typing import Any


class Storage(ABC):
    """Abstract interface shared by all storage implementations."""

    @abstractmethod
    def save(self, key: str, data: Any) -> None:
        """Save data under a key."""
        raise NotImplementedError

    @abstractmethod
    def get(self, key: str) -> Any:
        """Retrieve data by key, or raise KeyError if missing."""
        raise NotImplementedError

    @abstractmethod
    def delete(self, key: str) -> None:
        """Delete a record by key, or raise KeyError if missing."""
        raise NotImplementedError
