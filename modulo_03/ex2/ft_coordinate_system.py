#!/usr/bin/env python3
import math


def get_player_pos() -> None:
    while True:
        try:
            text = input("Enter new coordinates as "
                         "floats in format 'x,y,z': ")
            cord = text.split(',')
            coord = (float(cord[0]), float(cord[1]), float(cord[2]))
            break
        except ValueError:
            print('Invalid syntax')
    return (coord)


def calculate_dist(c1, c2=(0, 0, 0)) -> float:
    distance = math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2
                         + (c1[2] - c2[2])**2)
    return (distance)


if __name__ == "__main__":
    print('=== Game Coordinate System ===\n')
    c1 = get_player_pos()
    print("\nEnter new coordinates as floats informat 'x,y,z': "
          f"{c1[0]} , {c1[1]} , {c1[2]}")
    print(f'Got a first tuple: {c1}')
    print(f'It includes: X={c1[0]}, Y={c1[1]}, Z={c1[2]}')
    distance = round(calculate_dist(c1), 4)
    print(f'Distance to center: {distance}')
    c2 = get_player_pos()
    print("\nEnter new coordinates as floats informat 'x,y,z': "
          f"{c1[0]} , {c1[1]} , {c1[2]}")
    distance = round(calculate_dist(c1, c2), 4)
    print(f'Distance between the 2 sets of coordinates: {distance}')
