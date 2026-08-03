from ex0.creature import Creature
from .abs_capabilities1 import HealCapability as HC, TransformCapability as TC


class Sproutling(Creature, HC):
    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HC):
    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TC):
    def __init__(self, type_c):
        super().__init__(type_c)
        self._transform = False

    def attack(self) -> str:
        if self._transform is True:
            return "Shiftling performs a boosted strike!"
        else:
            return "Shiftling attacks normally"

    def transform(self) -> str:
        self._transform = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self._transform = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TC):
    def __init__(self, type_c):
        super().__init__(type_c)
        self._transform = False

    def attack(self) -> str:
        if self._transform is True:
            return "Morphagon unleashes a devastating morph strike!"
        else:
            return "Morphagon attacks normally."

    def transform(self) -> str:
        self._transform = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._transform = False
        return "Morphagon stabilizes its forms."
