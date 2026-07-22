#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    def __init__(self):
        self._items: list[str] = []
        self.__rank_counter = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check wether the input 
        data are appropriate for the current 
        data processor"""
        pass
    @abstractmethod
    def ingest(self, data: Any) -> None:
        """process the input data"""
        if not self.validate(data):
            raise ValueError("Improper data")
        
    def output(self) -> tuple[int, str]:
        if not self._items:
            return None
        self.__rank_counter += 1
        return (self._items.pop(0), self.__rank_counter)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float))for x in data)
        else:
            return False
    def ingest(self, data: int | float | list[int | float]) -> None:
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
        else:
            return False
    def ingest(self, data: str | list[str]) -> None:
        super().ingest(data)
        elemento = data if isinstance(data, list) else [data]
        for elem in elemento:
            self._items.append(elem)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(k, str) and isinstance(v, str)  for k, v in data.items())
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        else:
            return False


    def ingest(self, data: dict[str,str] | list[dict[str, str]]) -> None:
        super().ingest(data)
        elementos = [data] if isinstance(data, dict) else data
        for elem in elementos:
            text = ": ".join(elem.values())
            self._items.append(text)
        pass



def main():
    
    try:
        numerico = NumericProcessor()
        numerico.ingest("aba")
    except ValueError as ex:
        print(ex)


if __name__ == "__main__":
    main()