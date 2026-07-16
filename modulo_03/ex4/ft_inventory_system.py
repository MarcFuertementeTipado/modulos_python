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
            inventory.update({str(item[0]): int(item[1])})
        except ValueError as ex:
            print(ex)
    return inventory


if __name__ == "__main__":
    inventory = {}
    print('=== Inventory System Analysis ===\n')
    inventory = set_inventory()
    if not inventory:
        print('No items added, ending program')
        sys.exit()
    total_values = sum(inventory.values())
    print(f'Got inventory: {inventory}')
    print(f'Item list: {inventory.keys()}')
    print(f'Total quantity of the {len(inventory.keys())} items: '
          f'{total_values}')
    max_item: str = list(inventory.keys())[0]
    min_item: str = list(inventory.keys())[0]
    for item in inventory.keys():
        print(f'Item {item} represents '
              f'{round((inventory[item] * 100 / total_values), 1)}')
        if inventory[item] > inventory[max_item]:
            max_item = item
        if inventory[item] < inventory[min_item]:
            min_item = item
    print(f'Item most abundant: {max_item} with {inventory[max_item]}')
    print(f'Item lest abundant: {min_item} with {inventory[min_item]}')
    print(f'Updated inventory: {inventory}')
