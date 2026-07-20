#!/usr/bin/env python3
import sys
import typing


def main():
    if len(sys.argv) < 2:
        print('Usage: ./ft_ancient_text.py <file>')
        return
    try:
        print('=== Cyber Archives Recovery ===')
        print(f"Accessing file {sys.argv[1]}")
        with open(sys.argv[1], 'r') as archivo:
            contenido = archivo.read()
            print('---\n')
            print(contenido)
            print('---\n')
        print(f"File '{sys.argv[1]}' closed.")
    except FileNotFoundError as ex:
        print(f"Error opening file '{sys.argv[1]}': ", ex)
    except PermissionError as ex:
        print(f"Error opening file '{sys.argv[1]}'", ex)


if __name__ == "__main__":
    main()
