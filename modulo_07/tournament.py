#!/usr/bin/env python3
import ex2
import ex1
import ex0


def battle(opponets: list[tuple[ex0.CF, ex2.BS]]):
    print(f'{len(opponets)} opponents involved')
    try:
        for i in range(len(opponets)):
            actual_creature, actual_battle = opponets[i]
            ac = actual_creature.create_base()
            for j in range(i + 1, len(opponets)):
                print('* BATTLE *')
                print(ac.describe())
                print(' vs')
                next_creature, next_battle = opponets[j]
                nc = next_creature.create_base()
                print(nc.describe())
                print(' now fight!')
                actual_battle.act(ac)
                next_battle.act(nc)
                print()
    except TypeError as ex:
        print('Battle error, aborting tournament:', ex)


def main():
    # factories, strategies and list with creatures
    f = (ex0.FF(), ex0.AF(), ex1.HCF(), ex1.TCF())
    s = (ex2.NS(), ex2.AS(), ex2.DS())
    tournament1 = [(f[0], s[0]),
                   (f[2], s[2])]
    tournament2 = [(f[0], s[1]),
                   (f[2], s[2])]
    tournament3 = [(f[1], s[0]),
                   (f[2], s[2]),
                   (f[3], s[1])]
    # Tournaments
    print('== Tournament 0 ==')
    battle(tournament1)
    print('\n== Tournament 1 ==')
    battle(tournament2)
    print('\n== Tournament 2 ==')
    battle(tournament3)


if __name__ == "__main__":
    main()
