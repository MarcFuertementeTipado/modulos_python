#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name.capitalize()
        self._height = 0.0
        self._days = 0
        self.set_height(height)
        self.set_age(days)

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._days} days old")

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = round(new_height, 2)

    def set_age(self, new_days: int) -> None:
        if new_days < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = new_days

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days


class Flower(Plant):
    def __init__(self, name, height, days, color: str) -> None:
        self.set_color(color)
        super().__init__(name, height, days)

    def show(self) -> None:
        super().show()
        print(f'Color: {self._color}')

    def set_color(self, new_color: str) -> None:
        self._color = new_color

    def get_color(self) -> str:
        return self._color

    def bloom(self) -> None:
        print(f'{self._name} has not bloomed yet')
        print(f'[Asking the {self._name} to bloom]')
        self.show()
        print(f'{self._name} is blooming beautifully!')


class Tree(Plant):
    def __init__(self, name, height, days, trunk_diameter: float) -> None:
        self._trunk_diameter = 0.0
        self.set_trunk_diameter(trunk_diameter)
        super().__init__(name, height, days)

    def set_trunk_diameter(self, new_diameter: float) -> None:
        if new_diameter < 0:
            print(f'{self._trunk_diameter}: Error, can be negative')
            print('diameter update regeted')
        else:
            self._trunk_diameter = round(new_diameter, 2)

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def show(self) -> None:
        super().show()
        print(f'Diameter: {self._trunk_diameter}')

    def produce_shade(self) -> None:
        print(f'[Asking the {self._name} to produce shade]')
        print('Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.')


class Vegetable(Plant):
    def __init__(
            self,
            name,
            height,
            days, harvest_season: str, nutritional_value: int) -> None:
        self.set_harvest_season(harvest_season)
        self._nutritional_value = 0
        super().__init__(name, height, days)
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f'Harvest season: {self._harvest_season}')
        print(f'Nutritional value: {self._nutritional_value}')

    def set_harvest_season(self, new_season: str) -> None:
        self._harvest_season = new_season

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def get_nutritional_value(self) -> int:
        return self._nutritional_value

    def set_nutritional_value(self, new_n_value: int) -> None:
        if new_n_value < 0:
            print('Error: can be negative')
            print('Nutritional value update regeted')
        else:
            self._nutritional_value = new_n_value

    def set_age(self, new_days: int) -> None:
        super().set_age(new_days)
        self._nutritional_value += 1

    def set_grow(self, new_height: float) -> None:
        super().set_height(new_height)
        self._nutritional_value += 1


if __name__ == "__main__":
    print('=== Garden Plant types ===')
    print('=== Flower')
    flower = Flower('rose', 15, 10, 'red')
    flower.show()
    flower.bloom()
    print('\n=== Tree')
    tree = Tree('oak', 200, 365, 5)
    tree.show()
    tree.produce_shade()
    print('\n=== Vegetable')
    vegetable = Vegetable('tomato', 5, 10, 'Abril', 0)
    vegetable.show()
    vegetable.set_age(vegetable.get_age() + 20)
    vegetable.set_height(vegetable.get_height() + 20)
    vegetable.show()
