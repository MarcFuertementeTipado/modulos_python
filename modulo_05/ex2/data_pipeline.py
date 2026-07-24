#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Protocol


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

    def output(self) -> tuple[int, str] | None:
        if not self._items:
            return None
        self._rank_counter += 1
        return (self._rank_counter, self._items.pop(0))


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
        print("=== DataStream statistics ===")
        for proc in self._processors:
            print(proc.__class__.__name__, end="")
            print(f": total "
                  f"{proc._rank_counter + 1 + len(proc._items)}"
                  " items processed"
                  f", remaining {len(proc._items)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for p in self._processors:
            tuple_list: list[tuple[int, str]] = []
            for _ in range(nb):
                item = p.output()
                if item is not None:
                    tuple_list.append(item)
            # Si hay elementos, los procesamos con el plugin
            if tuple_list:
                plugin.process_output(tuple_list)


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExport():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        csv: str = ",".join([str(item[1]) for item in data])
        print('CSV Output:')
        print(csv)


class JSONExport():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        json = {item[0]: item[1] for item in data}
        print('JSON Output:')
        print(json)


def main() -> None:
    ds = DataStream()
    my_list = ['Hello world', [3.14, -1, 2.71],
               [{'log_level': 'WARNING', 'log_message': 'Telnet access!'},
               {'log_level': 'INFO', 'log_message': 'User wil isconnected'}],
               42, ['Hi', 'five']]
    num = NumericProcessor()
    tex = TextProcessor()
    log = LogProcessor()
    print('=== Code Nexus - Data Pipeline ===')
    print('\nInitialize Data Stream...\n')
    ds.register_processor(num)
    ds.register_processor(tex)
    ds.register_processor(log)
    print(f'\nSend first batch of data on stream: {my_list}\n')
    ds.process_stream(my_list)
    ds.print_processors_stats()
    print('\nSend 3 processed data from each processor to a CSV plugin: ')
    csv = CSVExport()
    json = JSONExport()
    ds.output_pipeline(3, csv)
    ds.print_processors_stats()
    sec_list = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
                [{'log_level': 'ERROR', 'log_message': '500 server crash'},
                {'log_level': 'NOTICE', 'log_message': 'Certificateexpires'}],
                [32, 42, 64, 84, 128, 168], 'World hello']
    ds.process_stream(sec_list)
    print(f'\nSend another batch of data: {sec_list}\n')
    ds.print_processors_stats()
    print('\nSend 5 processed data from each processor to a JSON plugin: ')
    ds.output_pipeline(5, json)
    print()
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
