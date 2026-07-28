#!/usr/bin/env python3
from .. import elements as el
from .. import potions as pt
import elements as e


def lead_to_gold() -> str:
    return "Recipe transmuting Lead to Gold: brew ’" \
           f"{el.create_air()}’ and ’{pt.strength_potion()}’ " \
           f"mixed with ’{e.create_fire()}’"
