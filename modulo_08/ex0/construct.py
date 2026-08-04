#!/usr/bin/env python3
import sys
import os
import site


def realworld_output() -> None:
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current python: {sys.executable}")
    venv_name = os.path.basename(sys.prefix)
    print(f"Virtual Enviroment: {venv_name}")
    print(f"Enviroment path: {sys.prefix}\n")
    print("SUCCESS: You're in an isolated enviroment!\n"
          "Safe to install packages without affecting\n"
          "the global system\n")
    print(f"Package installation path:\n {site.getsitepackages()[0]}")


def matrix_output() -> None:
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virutal Enviroment: None detected\n")
    print("To enter the construct, run:\n"
          "python3 -m venv matrix_env\n"
          "source matrix_env/bin/activate # On Unix\n"
          "matrix_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")


def main():
    if sys.prefix == sys.base_prefix:
        matrix_output()
    else:
        realworld_output()


if __name__ == "__main__":
    main()
