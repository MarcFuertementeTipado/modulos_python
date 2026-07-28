#!/usr/bin/env python3
from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ing_list = light_spell_allowed_ingredients()
    for ing in ing_list:
        if ingredients.find(ing) != -1:
            return f"({ingredients} - VALID)"
    return f"({ingredients} - INVALID)"
