# coding=utf-8
"""Parameters action abstraction."""

from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from splinter.driver import DriverAPI
from pbraiders.pages.options.parameters import ParametersPage


@dataclass
class ParametersActionAbstract(ABC):
    """Parameters action abstraction."""
    _page: ParametersPage

    @property
    def page(self) -> DriverAPI:
        """Returns driver instance."""
        return self._page.page
