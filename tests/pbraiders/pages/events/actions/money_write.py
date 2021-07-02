# coding=utf-8
"""Event page - choose money radio button responsability."""

from __future__ import annotations
from pbraiders.pages.events.actions import RADIO_MONEY
from pbraiders.pages.events.actions import EventActionAbstract


class EventMoneyWriteAction(EventActionAbstract):

    def choose(self) -> None:
        """Choose a value in the arrh radio buttons group."""
        self.page.choose(RADIO_MONEY, self.event.arrh)
