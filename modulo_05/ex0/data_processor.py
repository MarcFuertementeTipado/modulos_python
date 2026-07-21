#!/usr/bin/env python3
from abc import ABC
import typing 

class DataProcessor(ABC):
    @abstractmethod
    def validate():
        """Check wether the input 
        data are appropriate for the current 
        data processor"""
        
        pass
    @abstractmethod
    def ingest():
        """process the input data"""
        pass
    pass


class NumericProcessor(DataProcessor):
    pass


class TextProcessor(DataProcessor):
    pass


class LogProcessor(DataProcessor):
    pass