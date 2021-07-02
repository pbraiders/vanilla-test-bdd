# coding=utf-8
"""Event page - read fields responsability."""

from __future__ import annotations
from pbraiders.pages.events.actions import FIELD_REAL
from pbraiders.pages.events.actions import FIELD_PLANNED
from pbraiders.pages.events.actions import FIELD_CANCELED
from pbraiders.pages.events.actions import FIELD_MAX
from pbraiders.pages.events.actions import EventActionAbstract


class EventHeadcountReadAction(EventActionAbstract):

    def is_valid_real(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_REAL)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value).lower() == str(self.event.headcount.real).lower()

    def is_valid_planned(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_PLANNED)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value).lower() == str(self.event.headcount.planned).lower()

    def is_valid_canceled(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_CANCELED)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value).lower() == str(self.event.headcount.canceled).lower()

    def is_valid_max(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_MAX)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value).lower() == str(self.event.headcount.max).lower()
