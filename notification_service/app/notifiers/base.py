from abc import ABC, abstractmethod


class BaseNotifier(ABC):
    @abstractmethod
    async def send(self, user: dict, message: str) -> bool:
        pass
