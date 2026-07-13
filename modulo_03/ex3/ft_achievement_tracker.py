#!/usr/bin/env python3
import random


class Player():
    def __init__(self, name):
        self.name = name.capitalize()
        self.achi = set(gen_player_achievements())

    def show(self) -> None:
        print(f'Player {self.name} {self.achi}\n')


# Genera logros aleatorios y devuelve el set() con los logros
def gen_player_achievements():
    achievements = ["Boss Slayer",
                    "Collector Supreme",
                    "Crafting Genius",
                    "First Steps",
                    "Master Explorer",
                    "Sharp Mind",
                    "Speed Runner",
                    "Strategist",
                    "Survivor",
                    "Treasure Hunter",
                    "Unstoppable",
                    "Untouchable",
                    "World Savior"]
    player = set(random.sample(achievements,
                 random.randint(1, len(achievements))))
    return player


if __name__ == "__main__":
    print('=== Achievement Tracker System ===\n')
    p1 = Player('jose')
    p1.show()
    p2 = Player('bryan')
    p2.show()
    p3 = Player('adele')
    p3.show()
    p4 = Player('marcos')
    p4.show()
    print(f'Common achievements: {p1.achi & p2.achi & p3.achi & p4.achi}\n')
    print(f'Only {p1.name} has: '
          f'{p1.achi.difference(p2.achi, p3.achi, p4.achi)}')
    print(f'Only {p2.name} has: '
          f'{p2.achi.difference(p1.achi, p3.achi, p4.achi)}')
    print(f'Only {p3.name} has: '
          f'{p3.achi.difference(p2.achi, p1.achi, p4.achi)}')
    print(f'Only {p4.name} has: '
          f'{p4.achi.difference(p2.achi, p3.achi, p1.achi)}')
    all_achi = p1.achi | p2.achi | p3.achi | p4.achi
    print(f'\n{p1.name} is missing: {all_achi.difference(p1.achi)}')
    print(f'{p2.name} is missing: {all_achi.difference(p2.achi)}')
    print(f'{p3.name} is missing: {all_achi.difference(p3.achi)}')
    print(f'{p4.name} is missing: {all_achi.difference(p4.achi)}')
