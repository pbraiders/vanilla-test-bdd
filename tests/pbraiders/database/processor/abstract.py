# coding=utf-8
"""Database Processor Abstract Adapter"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pbraiders.database.adapter import AbstractAdapter


@dataclass
class AbstractProcessor(ABC):

    _pAdapter: AbstractAdapter

    @abstractmethod
    def execute(self, config: dict = None):
        pass
