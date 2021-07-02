# coding=utf-8
"""Contact action abstraction."""

from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from splinter.driver import DriverAPI
from pbraiders.pages.contacts import ContactPageAbstract
from pbraiders.contact import Contact


@dataclass
class ContactActionAbstract(ABC):
    """Contact action abstraction."""
    _page: ContactPageAbstract

    @property
    def page(self) -> DriverAPI:
        """Returns driver instance."""
        if self._page.page is None:
            raise TypeError("Driver is not set!")
        return self._page.page

    @property
    def contact(self) -> Contact:
        """Returns contact instance."""
        if self._page.contact is None:
            raise TypeError("Contact is not set!")
        return self._page.contact
