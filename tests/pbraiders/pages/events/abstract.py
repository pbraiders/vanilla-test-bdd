# coding=utf-8
"""Event page extended abstraction."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from pbraiders.pages import PageAbstract
from pbraiders.contact import Contact
from pbraiders.event import Event


@dataclass
class EventPageAbstract(PageAbstract):
    """Event page extended abstraction."""
    _event: Optional[Event] = None
    _contact: Optional[Contact] = None

    @property
    def event(self) -> Event | None:
        """Event getter."""
        return self._event

    @event.setter
    def event(self, event: Event) -> None:
        """Event setter."""
        self._event = event

    @event.deleter
    def event(self) -> None:
        """Event deleter."""
        self._event = None

    @property
    def contact(self) -> Contact | None:
        """Contact getter."""
        return self._contact

    @contact.setter
    def contact(self, contact: Contact) -> None:
        """Contact setter."""
        self._contact = contact

    @contact.deleter
    def contact(self) -> None:
        """Contact deleter."""
        self._contact = None
