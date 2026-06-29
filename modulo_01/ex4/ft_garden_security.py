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
