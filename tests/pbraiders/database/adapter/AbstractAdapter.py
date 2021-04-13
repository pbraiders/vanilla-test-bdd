# coding=utf-8
"""Database Abstract Adapter"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class AbstractAdapter(ABC):
    host: str = 'localhost'
    port: str = 3306
    user: str = ''
    password: str = ''
    database: str = ''
    charset: str = 'utf8mb4'

    @abstractmethod
    def quit(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, query: str, args: dict = None):
        pass
