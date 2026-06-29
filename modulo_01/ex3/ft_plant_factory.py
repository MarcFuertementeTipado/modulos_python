#!/usr/bin/env python3
class Plant:
    firts_h: float

    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name.capitalize()
        self.height = round(height, 2)
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
    plants_list = []
    plants_list.append(Plant('manuel', 25.555, 5))
    plants_list.append(Plant('jefa', 3, 1))
    plants_list.append(Plant('josefa', 4, 2))
    plants_list.append(Plant('maria', 10, 4))
    plants_list.append(Plant('mariano', 20, 6))
    print('=== Plant Factory Output ===')
    for i in plants_list:
        print('Created: ', end='')
        i.show()
