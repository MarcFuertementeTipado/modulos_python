#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check wether the input 
        data are appropriate for the current 
        data processor"""
        pass
    # @abstractmethod
    # def ingest(self, data: Any) -> None:
    #     """process the input data"""
    #     pass
    # def output(self) -> tuple[int, str]:
    #     pass


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, tuple):
            return all(isinstance(x, (int, float))for x in data)
        else:
            return False


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        else:
            return False


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(k, str) and isinstance(v, str)  for k, v in data.items())
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)


if __name__ == "__main__":
    numerico = NumericProcessor()
    print(numerico.validate((4, 5.5)))

    letras = TextProcessor()
    print(letras.validate(("hola", "adios")))

    diccionario = LogProcessor()
    print(diccionario.validate(["hola", "adios"]))
    