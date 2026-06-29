#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f'{self.name}: {self.height}cm, {self.age} days old')


if __name__ == "__main__":
    plant1 = Plant('rose', 25, 30)
    plant2 = Plant('claudia', 23, 23)
    plant3 = Plant('claudio', 45, 3)
    print('=== Garden Plant Registry ===')
    plant1.show()
    plant2.show()
    plant3.show()
