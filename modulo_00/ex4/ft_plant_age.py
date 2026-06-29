def ft_plant_age():
    min_days = 60
    days: int = int(input('Enter plant age in days: '))
    if days <= min_days:
        print('Plant needs more time to grow.')
    else:
        print('Plant is ready to harvest!')
