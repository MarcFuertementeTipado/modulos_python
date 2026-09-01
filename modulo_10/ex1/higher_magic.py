from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"you heal {target} with {power} power"


def attack(target: str, power: int) -> str:
    return f"you attack {target} with {power} power"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def super_spell(target: str, power: int) -> tuple[str, str]:
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return (result1, result2)
    return super_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def max_spell(target: str, power: int) -> str:
        new_power = power * multiplier
        return base_spell(target, new_power)
    return max_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_true(target: str, power: int) -> str:
        if condition(target, power):
            result = spell(target, power)
            return result
        else:
            return "Spell fizzled"
    return conditional_true


def spell_sequence(spells: list[Callable]) -> Callable:
    def invoke_all(target: str, power: int) -> list[str]:
        all_spells: list[str] = []
        for spell in spells:
            result = spell(target, power)
            all_spells.append(result)
        return all_spells
    return invoke_all


def main() -> None:
    # Run 'python3 data_generator.py' if u want get data for this ejercice
    all_spells: list[Callable] = [attack, heal]

    # menu options
    print('0: spell combiner')
    print('1: power amplifier')
    print('2: conditional caster')
    print('3: spell sequence')
    choise = input('chose function:\n')

    match choise:
        case '0':
            print('== spell combiner ==')
            new_combine = spell_combiner(heal, attack)
            print(new_combine("Dragon", 17))
        case '1':
            print('== power amplifier ==')
            new_spell = power_amplifier(attack, 20)
            print(new_spell('dragon', 5))
        case '2':
            print('== conditional caster ==')
            new_spell = conditional_caster(
                lambda target, power: power > 50, attack
            )
            print(new_spell('Dragon', 51))
        case '3':
            print('== Spell sequence ==')
            new_spells = spell_sequence(all_spells)
            print(new_spells('Dragon', 20))


if __name__ == "__main__":
    main()
