from abc import ABC, abstractmethod


class Creature(ABC):
    # Constructor
    def __init__(self, type_c: str):
        self.set_name(self.__class__.__name__)
        self.set_typec(type_c)

    # Getters
    def get_name(self) -> str:
        return self._name

    def get_typec(self) -> str:
        return self._typec

    # Setters
    def set_name(self, new_name: str) -> None:
        self._name = new_name

    def set_typec(self, new_type: str) -> None:
        self._typec = new_type

    # Methods
    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.get_name()} is a {self.get_typec()} type Creature"
