from ex0 import CF
from .creatures1 import Bloomelle, Sproutling, Shiftling, Morphagon


class HealingCreatureFactory(CF):
    def create_base(self) -> Sproutling:
        return Sproutling("Grass")

    def create_evolved(self) -> Bloomelle:
        return Bloomelle("Grass/Fairy")


class TransformCreatureFactory(CF):
    def create_base(self) -> Shiftling:
        return Shiftling("Normal")

    def create_evolved(self) -> Morphagon:
        return Morphagon("Normal/Dragon")
