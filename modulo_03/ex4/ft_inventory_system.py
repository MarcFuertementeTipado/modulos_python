#!/usr/bin/env python3
import sys

def set_inventory():
    inventory = {}
    for argv in sys.argv[1:]:
        try:
            if ":" not in argv:
                raise ValueError(f'Error - invalid parameter {argv}')
            item = argv.split(":")
            if not item[0].isalpha():
                raise ValueError(f'{argv} does not exist...')
            if not int(item[1]):
                raise ValueError(f"Quantity error for '{item[0]}': "
                                 f"invalid literal for int() with "
                                 f"base 10: '{item[1]}'")
            if item[0] in inventory.keys():
                raise ValueError(f"Redundant item '{item[0]}'"
                                 f" - discarging")
            inventory.update({str(item[0]):int(item[1])})
        except ValueError as ex:
            print(ex)
    return inventory


if __name__ == "__main__":
    inventory = {"espada": 2}
    print('=== Inventory System Analysis ===\n')
    inventory = set_inventory()
    print(f'Got inventory: {inventory}')
