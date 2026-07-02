#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    try:
        inp: str = '25'
        print('=== Garden Temperature ===')
        print(f'\nInput data is {inp}')
        num: int = input_temperature(inp)
        print(f'Temperature is now {num}°C')
        print('All test completed - program didn\'t crash!')
    except ValueError:
        print(f'Caught input_temperature error: '
              f'invalid literal for int()'
              f' with base 10: \'{inp}\'')
    except Exception:
        print('Error!')
    finally:
        print('El programa sigue corriendo')


if __name__ == "__main__":
    test_temperature()
