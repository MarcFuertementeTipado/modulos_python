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


class DataStream():
    def __init__(self):
        self._processors: list[DataProcessor] = []
        for subclass in DataProcessor.__subclasses__():
            self._processors.append(subclass())

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for elem in stream:
            processed = False
            for processor in self._processors:
                if processor.validate(elem):
                    processor.ingest(elem)
                    processed = True
                    break
            if not processed:
                print(f"DataStream error - "
                      f"can't process element in stream: {elem}")

    def print_processors_stats(self) -> None:
        for processor in self._processors:
            print(processor.__class__.__name__)
            print(processor._items)


def main() -> None:
    print('=== Code Nexus - Data Stream')
    print('=== DataStream statistics ===')
    my_lista = [[1, 'hello'],'Hello world', [3.14, -1, 2.71], [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, {'log_level': 'INFO', 'log_message': 'User wil isconnected'}], 42, ['Hi', 'five']]
    ds = DataStream()
    ds.process_stream(my_lista)
if __name__ == "__main__":
    main()
