#!/usr/bin/env python3
class GardenError(Exception):
    def __init__(self, message='A basic garden error occurred.'):
        self.message = message


class PlantError(GardenError):
    def __init__(self, message='Unknown plant error.'):
        self.message = message


def water_plant(plant_name) -> None:
    if plant_name == plant_name.capitalize():
        print(f'Watering {plant_name}: [OK]')
    else:
        raise PlantError(f'Invalid plant name to water: {plant_name}')


def test_watering_system() -> None:
    names = ['Tomato', 'lettuce', 'Carrots']
    print('=== Garden Watering System ===')
    print('\nTesting valid plants...')
    print('Opening watering system')
    try:
        for case in names:
            water_plant(case)
    except PlantError as ex:
        print(f'Caught {ex.__class__.__name__}', ex)
        print('.. ending test and returning to main')
        return
    finally:
        print('Closing watering system')


if __name__ == "__main__":
    test_watering_system()
    print('\nCleanup always happens, even with errors!')
