from abc import ABC, abstractmethod
from .creature import Creature as CR


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> CR:
        pass

    @abstractmethod
    def create_evolved(self) -> CR:
        pass
    pass
