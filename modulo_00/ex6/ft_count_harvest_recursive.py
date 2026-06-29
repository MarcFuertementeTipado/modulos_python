def recursive(days, actual):
    """Funcion recursiva para imprimir los dias."""
    if actual > days:
        return
    print(f'Day {actual}')
    recursive(days, actual + 1)


def ft_count_harvest_recursive():
    """Funcion principal que maneja la entrada y la recursion."""
    try:
        user_input = input('Days until harvest: ')
        days = int(user_input)
        print(f'Days until harvest: {days}')
        recursive(days, 1)
        print('Harvest time!')
    except ValueError:
        print('Error: Debes ingresar un numero entero.')
