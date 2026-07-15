#!/usr/bin/env python3
import random


def main():
    inicial_list = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    cap_list = [palabra.capitalize() for palabra in inicial_list]
    only_cap_list = [palabra for palabra in inicial_list if palabra.istitle()]
    cap_dicc = {palabra: random.randrange(0,100) for palabra in cap_list}
    average_score = round(sum(cap_dicc.values()) / len(cap_dicc), 2)
    hig_dicc = {palabra: round(random.uniform(average_score, 100), 2) for palabra in cap_dicc}

    print("=== Gama Data Alchemist ===")
    print('Initial list of players: ',inicial_list)
    print('New list with all names capitalized: ',cap_list)
    print('New list of capitalized names only: ', only_cap_list)
    print('Score dict: ', cap_dicc)
    print(f'Score average: is {average_score}')
    print('Hight scores: ', hig_dicc)


if __name__ == "__main__":
    main()