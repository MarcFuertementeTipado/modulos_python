#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    test_cases = ["25", "abc"]
    print('=== Garden Temperature ===')
    for case in test_cases:
        try:
            print(f'\nInput data is {case}')
            num: int = input_temperature(case)
            print(f'Temperature is now {num}°C')
        except ValueError as er:
            print(f'{er}')
        except Exception:
            print('Error!')
    print('\nAll test completed - program didn\'t crash!')


if __name__ == "__main__":
    test_temperature()
