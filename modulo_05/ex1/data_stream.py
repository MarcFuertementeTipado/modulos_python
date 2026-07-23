#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._items: list[str] = []
        self._rank_counter = -1

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
        self._rank_counter += 1
        return (self._items.pop(0), self._rank_counter)


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
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)
        print(f'Registering {proc.__class__.__name__}')

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
        for proc in self._processors:
            print("=== DataStream statistics ===")
            print(proc.__class__.__name__, end="")
            print(f": total "
                  f"{proc._rank_counter + 1 + len(proc._items)}"
                  " items processed"
                  f", remaining {len(proc._items)} on processor")


def main() -> None:
    print('=== Code Nexus - Data Stream')
    print('=== DataStream statistics ===')
    ds = DataStream()
    numeric = NumericProcessor()
    ds.register_processor(numeric)
    my_list = ['Hello world', [3.14, -1, 2.71],
               [{'log_level': 'WARNING', 'log_message': 'Use ssh instead'},
                {'log_level': 'INFO', 'log_message': 'User wil isconnected'}],
               42, ['Hi', 'five']]
    print(f'Send data on stream: {my_list}\n')
    ds.process_stream(my_list)
    ds.print_processors_stats()
    print('\nSecon try, adding more types processors')
    text = TextProcessor()
    log = LogProcessor()
    ds.register_processor(text)
    ds.register_processor(log)
    print('Resending list again...')
    ds.process_stream(my_list)
    ds.print_processors_stats()
    ds._processors[0].output()
    ds._processors[1].output()
    ds._processors[2].output()
    print('\n   Removing 1 item from each processor...')
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
