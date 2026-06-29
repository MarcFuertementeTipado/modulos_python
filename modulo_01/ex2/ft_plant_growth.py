#!/usr/bin/env python3
class Plant:
    firts_h: float

    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.days = days
        self.firts_h = height

    def show(self) -> None:
        print(f'{self.name}: {self.height}cm, {self.days} days old')

    def grow(self, grow: float) -> None:
        self.height += grow
        self.height = round(self.height, 2)

    def age(self) -> None:
        self.days += 1


if __name__ == "__main__":
    plant = Plant('rose', 5, 3)
    print('=== Garden Plant Growth ===')
    plant.show()
    for i in range(1, 8):
        plant.grow(4.55)
        plant.age()
        print(f'=== Day {i} ===')
        plant.show()
    print(f'Growth this week: {plant.height - plant.firts_h}cm')
