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

    @property
    def contact(self) -> Contact | None:
        """Contact getter."""
        return self._contact

    def set_event(self, event: Event = None) -> EventPageAbstract:
        """Event setter."""
        self._event = event
        return self

    def set_contact(self, contact: Contact = None) -> EventPageAbstract:
        """Contact setter."""
        self._contact = contact
        return self
