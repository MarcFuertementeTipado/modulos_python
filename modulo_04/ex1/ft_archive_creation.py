#!/usr/bin/env python3
import sys
import typing


def transform_archivo(in_contenido: str):
    contenido = in_contenido.splitlines()
    print('Transform data:')
    print('---\n')
    for linea in contenido:
        linea = linea + '#'
        print(linea)
    print('\n---\n')
    name_file = input('Enter new file name(or empty):')
    if name_file:
        print(f'Saving data to {name_file}')
        archivo_escritura = open(name_file, 'w')
        for linea in contenido:
            linea = linea + '#\n'
            archivo_escritura.write(linea)
        archivo_escritura.close()
        print(f"Data saved in file '{name_file}'")


def leer_archivo(archivo: typing.IO):
    contenido = archivo.read()
    print('---\n')
    print(contenido)
    print('\n---\n')
    contenido = transform_archivo(contenido)


def main():
    if len(sys.argv) < 2:
        print('Usage: ./ft_ancient_text.py <file>')
        return
    try:
        print('=== Cyber Archives Recovery ===')
        print(f"Accessing file {sys.argv[1]}")
        archivo_abierto = open(sys.argv[1], 'r')
        leer_archivo(archivo_abierto)
        archivo_abierto.close()
        print(f"File '{sys.argv[1]}' closed.")
    except FileNotFoundError as ex:
        print(f"Error opening file '{sys.argv[1]}': ", ex)
    except PermissionError as ex:
        print(f"Error opening file '{sys.argv[1]}'", ex)


if __name__ == "__main__":
    main()
