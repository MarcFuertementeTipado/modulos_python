#!/usr/bin/env python3
class GardenError(Exception):
    def __init__(self, message='A basic garden error occurred.'):
        self.message = message


class PlantError(GardenError):
    def __init__(self, message='Unknown plant error.'):
        self.message = message


class WaterError(GardenError):
    def __init__(self, message='Unknown watering error'):
        self.message = message


def check_water() -> None:
    raise WaterError('Not enough water in the tank!')


def check_plant() -> None:
    raise PlantError('The tomato plant is wilting!')


def test_exceptions() -> None:
    print('=== Custon Garden Errors Demo ===\n')
    try:
        print('\nTestint PlantError...')
        check_plant()
    except PlantError as ex:
        print(f'Caugh {ex.__class__.__name__}: ', ex)
    try:
        print('\nTesting WaterError...')
        check_water()
    except WaterError as ex:
        print(f'Caugh {ex.__class__.__name__}: ', ex)
    print('\nTesting catching all garden errors...')
    try:
        check_plant()
    except GardenError as ex:
        print(f'Caugh {ex.__class__.__name__}: ', ex)

    try:
        check_water()
    except GardenError as ex:
        print(f'Caugh {ex.__class__.__name__}: ', ex)
    print('\nAll custom error types work correctly!')


if __name__ == '__main__':
    test_exceptions()
