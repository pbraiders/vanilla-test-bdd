
# coding=utf-8
"""Event page - choose money radio button responsability."""

from __future__ import annotations
from pbraiders.pages.events.actions import RADIO_MONEY
from pbraiders.pages.events.actions import EventActionAbstract


class EventMoneyReadAction(EventActionAbstract):

    def is_valid(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(RADIO_MONEY)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value).lower() == str(self.event.arrh).lower()
