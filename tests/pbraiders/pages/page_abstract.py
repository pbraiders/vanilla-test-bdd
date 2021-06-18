# coding=utf-8
"""Page abstraction."""

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from splinter.driver import DriverAPI


@dataclass
class PageAbstract(ABC):
    """Page abstraction."""
    _driver: DriverAPI
    _config: dict

    @abstractmethod
    def on_page(self) -> bool:
        """Returns True if we are visiting this page."""
        pass

    @abstractmethod
    def visit(self) -> bool:
        """Goes to the page"""
        pass

    @property
    def page(self) -> DriverAPI:
        """Driver getter"""
        return self._driver

    @property
    def config(self) -> dict:
        """Config getter"""
        return self._config
