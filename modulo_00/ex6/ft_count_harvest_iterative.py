def ft_count_harvest_iterative():
    days: int = int(input('Days until harvest: '))
    print(f'Days until harvest: {days}')
    for i in range(1, days + 1):
        print(f'Day: {i}')
    print('Harvest time!')
