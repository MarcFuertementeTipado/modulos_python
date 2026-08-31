# Funciones a transformar en lambda
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_list = sorted(artifacts, key=lambda x: x["power"], reverse=True)
    return sorted_list


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered_list = list(filter(lambda x: x['power'] >= min_power, mages))
    return filtered_list


def spell_transformer(spells: list[str]) -> list[str]:
    new_spells = list(
        map(lambda x: f"* {x} *", spells)
    )
    return new_spells


def mage_stats(mages: list[dict]) -> dict:
    min_item = min(mages, key=lambda x: x['power'])
    max_item = max(mages, key=lambda x: x['power'])
    average_item = round(sum(m['power'] for m in mages) / len(mages), 2)
    return {'max_power': max_item['power'],
            'min_power': min_item['power'],
            'avg_power': average_item}


def main() -> None:
    # Lists we are gonna use
    # can be changed by new lists generated in data_generator.py
    artifacts = [{'name': 'Storm Crown', 'power': 88, 'type': 'weapon'},
                 {'name': 'Wind Cloak', 'power': 79, 'type': 'weapon'},
                 {'name': 'Crystal Orb', 'power': 103, 'type': 'focus'},
                 {'name': 'Ice Wand', 'power': 69, 'type': 'armor'}]

    mages = [{'name': 'Morgan', 'power': 52, 'element': 'fire'},
             {'name': 'Alex', 'power': 86, 'element': 'shadow'},
             {'name': 'Luna', 'power': 72, 'element': 'earth'},
             {'name': 'Riley', 'power': 77, 'element': 'earth'},
             {'name': 'Ember', 'power': 50, 'element': 'water'}]

    spells = ['lightning', 'darkness', 'tornado', 'meteor']

    # Choosing which function do we wanna test
    print('0: artifact_sorter')
    print('1: power_filter')
    print('2: spell transformer')
    print('3: mage stats')
    chose = input("Which function do u wanna test?\n")
    end_list: list = []
    end_dic: dict = {}

    match chose:
        case '0':
            print('== artifact sorter ==')
            end_list = artifact_sorter(artifacts)
        case '1':
            try:
                print('== power filter ==')
                power = int(input('Choose minimum power\n'))
                end_list = power_filter(mages, power)
            except ValueError as ex:
                print(ex)
        case '2':
            print('== spell transformer ==')
            end_list = spell_transformer(spells)
        case '3':
            print('== mage stats ==')
            end_dic = mage_stats(mages)

    # print the results
    if end_list:
        for item in end_list:
            print(item)
    elif end_dic:
        print(end_dic)


if __name__ == "__main__":
    main()
