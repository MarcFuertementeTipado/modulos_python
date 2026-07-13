#!/usr/bin/env python3
import sys

def set_inventory():
    for argv in sys.argv[1:]:
        try:
            print(argv)
            if ":" not in argv:
                raise ValueError(f'Error - invalid parameter {argv}')

        except ValueError as ex:
            print(ex)

if __name__ == "__main__":
    inventory = {"espada": 2}
    print('=== Inventory System Analysis ===\n')
    set_inventory()
