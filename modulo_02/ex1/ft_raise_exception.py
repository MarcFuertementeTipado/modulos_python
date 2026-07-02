#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)
    if temp > 40:
        raise ValueError(f'Caught input_temperature error: '
                         f'{temp}°C is too hot for plants (max 40°C)')
    if temp < 0:
        raise ValueError(f'Caught input_temperature error: '
                         f'{temp}°C is too cold for plants (min 0°C)')

    else:
        return temp


def test_temperature() -> None:
    test_cases = ["25", "abc", "100", "-50"]
    print('=== Garden Temperature ===')
    for case in test_cases:
        try:
            print(f'\nInput data is {case}')
            num: int = input_temperature(case)
            print(f'Temperature is now {num}°C')
        except ValueError as er:
            print(f"{er}")
        except Exception:
            print('Error!')
    print('\nAll test completed - program didn\'t crash!')

if __name__ == "__main__":
    test_temperature()
