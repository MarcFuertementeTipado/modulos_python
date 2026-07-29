from .abs_factory import CreatureFactory as fact
from .creatures import Flameling, Aquabub, Pyrodon, Torragon


class FlameFactory(fact):
    def create_base(self) -> Flameling:
        return Flameling("Fire")

    def create_evolved(self) -> Pyrodon:
        return Pyrodon("Fire/Flying")


class AquaFactory(fact):
    def create_base(self) -> Aquabub:
        return Aquabub("Water")

    def create_evolved(self) -> Torragon:
        return Torragon("Water")
