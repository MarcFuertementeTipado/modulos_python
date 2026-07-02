#!/usr/bin/env python3
class Plant:
    class Data:
        def __init__(self) -> None:
            self._total_grow = 0
            self._total_age = 0
            self._total_show = 0

        def display_stats(self) -> None:
            print('[Statics]')
            print(f'grow: {self._total_grow} '
                  f'age: {self._total_age} show: {self._total_show}')

    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name.capitalize()
        self._height = 0.0
        self._days = 0
        self.data = self.Data()
        self.set_height(height)
        self.set_age(days)

    def show(self) -> None:
        self.data._total_show += 1
        print(f"{self._name}: {self._height}cm, {self._days} days old")

    @staticmethod
    def isolder_year(days: int) -> bool:
        if days > 365:
            return True
        else:
            return False

    @classmethod
    def anonymous_plant(cls):
        return cls('Unknow', 0, 0)

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.data._total_grow += 1
            self._height = round(new_height, 2)

    def set_age(self, new_days: int) -> None:
        if new_days < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.data._total_age += 1
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
    class Data(Plant.Data):
        def __init__(self) -> None:
            super().__init__()
            self._total_shade = 0

        def display_stats(self) -> None:
            super().display_stats()
            print(f'shade: {self._total_shade}')

    def __init__(self, name, height, days, trunk_diameter: float) -> None:
        self._trunk_diameter = 0.0
        super().__init__(name, height, days)
        self.data: Tree.Data = self.Data()
        self.set_trunk_diameter(trunk_diameter)

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
        self.data._total_shade += 1
        print(f'[Asking the {self._name} to produce shade]')
        print('Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.')


class Seed(Flower):
    def __init__(self, name, height, days, color, seed: int) -> None:
        self._seed = 0
        super().__init__(name, height, days, color)

    def bloom(self) -> None:
        print(f'{self._name} has not bloomed yet')
        print(f'[Asking the {self._name} to bloom]')
        self._seed = 20
        print(f'{self._name} is blooming beautifully!')

    def show(self) -> None:
        super().show()
        print(f'Seeds: {self._seed}')

    def get_seed(self) -> int:
        return self._seed

    def set_seed(self, new_seed) -> None:
        self._seed = new_seed


def visualizar_estadisticas(self, plant: Plant) -> None:
    self.plant.Data.display_stats()


if __name__ == "__main__":
    print('=== Garden statics ===')
    print('=== Check year-old')
    print(f'Is 30 days more than a year? -> {Plant.isolder_year(30)}')
    print(f'Is 400 days more than a year? -> {Plant.isolder_year(400)}')
    print('\n=== Flower')
    flower = Flower('rose', 15.00, 10, 'red')
    flower.bloom()
    flower.data.display_stats()
    print('\n=== Tree')
    tree = Tree('dak', 200, 365, 5.0)
    tree.data.display_stats()
    tree.produce_shade()
    tree.data.display_stats()
    print('\n=== Seed')
    seed = Seed('sunflower', 80, 45, 'yellow', 0)
    seed.show()
    seed.bloom()
    seed.data.display_stats()
    print('\n=== Anonymous')
    anonymous = Plant.anonymous_plant()
    anonymous.show()
    anonymous.data.display_stats()
