# coding=utf-8
"""Contact page extended abstraction."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from pbraiders.pages import PageAbstract
from pbraiders.contact import Contact


@dataclass
class ContactPageAbstract(PageAbstract):
    """Contact page extended abstraction."""
    _contact: Optional[Contact] = None

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
