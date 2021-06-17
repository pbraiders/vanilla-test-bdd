# coding=utf-8
"""Abstract contact action."""

from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from splinter.driver import DriverAPI
from pbraiders.contact import Contact
from pbraiders.contacts import ContactPageAbstract


@dataclass
class ActionContactAbstract(ABC):
    """Abstract contact action."""
    parent: ContactPageAbstract

    @property
    def contact(self) -> Contact:
        """Returns parent's contact instance."""
        if self.parent.contact is None:
            raise TypeError("Contact is not set!")
        return self.parent.contact

    @property
    def browser(self) -> DriverAPI:
        """Returns parent's driver instance."""
        if self.parent.browser is None:
            raise TypeError("Driver is not set!")
        return self.parent.browser
