#!/usr/bin/env python
def garden_operations(operation_number):
    match operation_number:
        case 0:
            int('abc')
        case 1:
            10 / 0
        case 2:
            open('noexisto.txt')
        case 3:
            2 + 'hola'
        case _:
            return


def test_error_types():
    num = [0, 1, 2, 3]
    for case in num:
        try:
            garden_operations(case)
        except Exception as ex:
            print(f'\nTesting operation {case}...\n'
                  f'Caught {ex.__class__.__name__}: {ex}')
    print('\nAll error types testd successfully!')


if __name__ == "__main__":
    test_error_types()
