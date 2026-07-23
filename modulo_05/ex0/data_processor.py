#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self):
        self._items: list[str] = []
        self.__rank_counter = -1

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check whether the input data are appropriate for the current
        data processor."""
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Process the input data."""
        if not self.validate(data):
            raise ValueError("Improper data")

    def output(self) -> tuple[str, int] | None:
        if not self._items:
            return None
        self.__rank_counter += 1
        return (self._items.pop(0), self.__rank_counter)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: int | float | list[int]
               | list[float] | list[int | float]) -> None:
        super().ingest(data)
        elementos = data if isinstance(data, list) else [data]
        for elem in elementos:
            self._items.append(str(elem))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        super().ingest(data)
        elemento = data if isinstance(data, list) else [data]
        for elem in elemento:
            self._items.append(elem)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
            )
        if isinstance(data, list):
            return all(isinstance(x, dict) for x in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        super().ingest(data)
        elementos = [data] if isinstance(data, dict) else data
        for elem in elementos:
            text = ": ".join(elem.values())
            self._items.append(text)


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    # NUMERIC PROCESSOR TEST
    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print(" Trying to validate input '42': ", end="")
    print(numeric.validate(42))
    print(" Trying to validate input 'Hello': ", end="")
    print(numeric.validate("Hello"))
    try:
        print(" Test invalid ingestion of string "
              "'foo' without prior validation:")
        numeric.ingest("foo")
    except ValueError as ex:
        print(" Got exception:", ex)

    num_list = [1, 2, 3, 4, 5]
    numeric.ingest(num_list)
    print(" Processing data:", num_list)
    print(" Extracting 3 values...")
    for _ in range(1, 4):
        num_tupla = numeric.output()
        if num_tupla:
            print(f" Numeric values {num_tupla[1]}:", num_tupla[0])

    # TEXT PROCESSOR TEST
    print("\nTesting Text Processor...")
    text = TextProcessor()
    print(" Trying to validate input '42': ", end="")
    print(text.validate(42))
    text_list = ["Hello", "Nexus", "World"]
    text.ingest(text_list)
    print(" Processing data:", text_list)
    print(" Extracting 1 value ...")
    tex_tupla = text.output()
    if tex_tupla:
        print(f" Text value {tex_tupla[1]}: {tex_tupla[0]}")

    # LOG PROCESSOR TEST
    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(" Trying to validate input 'Hello': ", end="")
    print(log.validate('Hello'))

    dic_list = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    log.ingest(dic_list)
    print(" Processing data:", dic_list)
    print(" Extracting 2 values...")
    for _ in range(1, 3):
        log_tupla = log.output()
        if log_tupla:
            print(f" log entry {log_tupla[1]}: {log_tupla[0]}")


if __name__ == "__main__":
    main()
