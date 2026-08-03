from abc import ABC, abstractmethod
from ex0 import creature


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature):
        pass

