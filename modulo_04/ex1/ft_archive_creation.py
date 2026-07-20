#!/usr/bin/env python3
import sys


def transform_data(data: str):
    f = open(data, 'r')
    contenido = f.read()
    lineas = contenido.splitlines()
    print('\nTransform Data:\n---\n')
    for linea in lineas:
        linea = linea + '#'
        print(linea)
    print('---\n')
    name = input('Enter new file name (or empty):')
    if name:
        new_file = open(name, 'w')
        for linea in lineas:
            new_file.write(linea + '#\n')
        print(f"Saving data to '{name}'")
    new_file.close()
    print('Data saved in file')


def print_file(txt: str):
    f = open(txt, 'r')
    contenido = f.read()
    print('---\n')
    print(contenido)
    print('---\n')
    f.close()
    print(f"File '{txt}' closed.")


def main():
    if len(sys.argv) < 2:
        print('Usage: ./ft_ancient_text.py <file>')
        return
    try:
        print('=== Cyber Archives Recovery ===')
        print(f"Accessing file {sys.argv[1]}")
        print_file(sys.argv[1])
        transform_data(sys.argv[1])
    except FileNotFoundError as ex:
        print(f"Error opening file '{sys.argv[1]}': ", ex)
    except PermissionError as ex:
        print(f"Error opening file '{sys.argv[1]}'", ex)


if __name__ == "__main__":
    main()
