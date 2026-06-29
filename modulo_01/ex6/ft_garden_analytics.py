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


class Seed(Flower):
    def __init__(self, name, height, days, color, seed: int) -> None:
        super().__init__(name, height, days, color)

    def bloom(self) -> bool:
        

    def show(self) -> None:
        super().show()
        print(f'Seeds: {self._seed}')

    def get_seed(self) -> int:
        return self._seed

    def set_seed(self, new_seed) -> None:
        self._seed = new_seed

# una clase Seed que hereda de Flower, almacena el numero de semillas una vez la Flower bloom. el show() debe evolucionar mostrando tmb dicha informacion
# Cada Plant tiene un sistema interno implementado como clase anidada que contiene datos estaticos. numero de grow(), age() show(). la encapsulacion es requerida
# Tree necesitan un pedazo de informacion estatica extra, numero de produce_shade() realizados
# crea una funcion unica que muestre informacion estatica para cualquier clase

if __name__ == "__main__":
    seed = Seed('mairposa', 10, 3, 'yellow', 5)
    seed.show()
    
