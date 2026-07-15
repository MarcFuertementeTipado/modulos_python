#!/usr/bin/env python3
import typing, random

def consume_event(my_list: list):
    while my_list:
        evento = my_list.pop(random.randrange(len(my_list)))
        yield evento

def gen_event():
    persons = ["Anna", "Jesus", "Maria", "Jose"]
    accions = ["Saltar", "Correr", "Animar", "Esconderse"]
    while True:
        yield (random.choice(persons), random.choice(accions))


def main():
    my_list = []
    generador = gen_event()
    for i in range(1000):
        print(f'{i + 1}: ',next(generador))
    for i in range(10):
        my_list.append(next(gen_event()))
    print('my lista: ',my_list)
    for evento in consume_event(my_list):
        print('evento consumido: ', evento)
        print('Queda en la lista: ', my_list)


if __name__ == "__main__":
    main()