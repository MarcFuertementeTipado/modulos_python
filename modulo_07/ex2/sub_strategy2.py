from .abs_strategy2 import BattleStrategy as BS
from ex0 import creature as cr
from ex1 import creatures1 as crs1


class NormalStrategy(BS):
    def is_valid(self, creature) -> bool:
        if isinstance(creature, cr.Creature):
            return True
        else:
            return False

    def act(self, creature: cr.Creature) -> None:
        if self.is_valid(creature) is False:
            raise TypeError('Invalid, this is not a creature...')
        print(creature.attack())


class AggressiveStrategy(BS):
    def is_valid(self, creature) -> bool:
        if isinstance(creature, (crs1.Morphagon, crs1.Shiftling)):
            return True
        else:
            return False

    def act(self, creature) -> None:
        if self.is_valid(creature) is False:
            raise TypeError('Invalid Creature for this agressive strategy')
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BS):
    def is_valid(self, creature) -> bool:
        if isinstance(creature, (crs1.Sproutling, crs1.Bloomelle)):
            return True
        else:
            return False

    def act(self, creature):
        if self.is_valid(creature) is False:
            raise TypeError('Invalid Creature for this Defensive strategy')
        print(creature.attack())
        print(creature.heal())
