#!/usr/bin/env python3
import sys
import typing


def leer_archivo(archivo: typing.IO) -> None:
    contenido = archivo.read()
    print('---\n')
    print(contenido)
    print('---\n')


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
