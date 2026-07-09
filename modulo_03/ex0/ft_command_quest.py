#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    arg: int = len(sys.argv)
    num: int = 1
    print('=== Command Quest ===')
    print(f'Program name: {sys.argv[0]}')
    if arg == 1:
        print('No arguments provided!')
    else:
        print(f'Arguments received: {arg - 1}')
        for i in sys.argv:
            print(f'Argument {num}: {i}')
            num += 1
    print(f'Total arguments: {arg}')
