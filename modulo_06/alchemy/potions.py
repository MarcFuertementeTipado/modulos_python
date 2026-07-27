#!/usr/bin/env python3
import elements as e
import alchemy.elements as ae


def healing_potion() -> str:
    return "Healing potion brewed with ’" \
           f"{ae.create_earth()}’ and ’{ae.create_air()}’"


def strength_potion() -> str:
    return "Strength potion brewedwith ’" \
           f"{e.create_fire()}’ and ’{e.create_water()}’"
