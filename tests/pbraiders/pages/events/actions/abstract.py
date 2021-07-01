# coding=utf-8
"""Contact action abstraction."""

from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from splinter.driver import DriverAPI
from pbraiders.contact import Contact
from pbraiders.event import Event
from pbraiders.pages.events import EventPageAbstract


@dataclass
class EventActionAbstract(ABC):
    """Event action abstraction."""
    _page: EventPageAbstract

    @property
    def page(self) -> DriverAPI:
        """Returns driver instance."""
        return self._page.page

    @property
    def contact(self) -> Contact:
        """Returns contact instance."""
        if self._page.contact is None:
            raise TypeError("Contact is not set!")
        return self._page.contact

    @property
    def event(self) -> Event:
        """Returns event instance."""
        if self._page.event is None:
            raise TypeError("Event is not set!")
        return self._page.event
