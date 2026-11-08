from abc import ABC, abstractmethod


class Notifier(ABC):
    @property
    @abstractmethod
    def channel_name(self):
        raise NotImplementedError

    @abstractmethod
    def send(self, customer, message: str) -> bool:
        raise NotImplementedError
