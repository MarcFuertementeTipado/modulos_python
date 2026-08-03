#!/usr/bin/env python3
import ex1


def main():
    hf = ex1.HCF()
    sp = hf.create_base()
    bl = hf.create_evolved()
    # First test
    print('== Testing Creature with healing capability ==')
    print('BASE:')
    print(sp.describe())
    print(sp.attack())
    print(sp.heal())
    print('EVOLVED:')
    print(bl.describe())
    print(bl.attack())
    print(bl.heal())
    # Second test
    print('\n== Testing Creature with transform capability ==')
    print('BASE:')
    tf = ex1.TCF()
    sf = tf.create_base()
    print(sf.describe())
    print(sf.attack())
    print(sf.transform())
    print(sf.attack())
    print(sf.revert())
    print('EVOLVED:')
    mph = tf.create_evolved()
    print(mph.describe())
    print(mph.attack())
    print(mph.transform())
    print(mph.attack())
    print(mph.revert())


if __name__ == "__main__":
    main()
