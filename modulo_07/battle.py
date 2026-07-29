#!/usr/bin/env python3
import ex0


def battle(f1: ex0.FF, f2: ex0.AF):
    c1 = f1.create_base()
    c2 = f2.create_base()
    print(c1.describe())
    print('vs')
    print(c2.describe())
    print(c1.attack())
    print(c2.attack())


def factory_checker(fact: ex0.CF):
    base_c = fact.create_base()
    evolved_c = fact.create_evolved()
    print(base_c.describe())
    print(base_c.attack())
    print(evolved_c.describe())
    print(evolved_c.attack())


def main() -> None:
    f_factory = ex0.FF()
    a_factory = ex0.AF()
    # Factory Test
    print('Testing Factory')
    factory_checker(f_factory)
    print('\nTesting Factory')
    factory_checker(a_factory)
    # Battle Test
    print('\nTesting battle')
    battle(f_factory, a_factory)


if __name__ == "__main__":
    main()
