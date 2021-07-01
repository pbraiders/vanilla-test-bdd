# coding=utf-8
"""Event page - choose money radio button responsability."""

from __future__ import annotations
from pbraiders.pages.events.actions import EventActionAbstract

RADIO_MONEY = 'reh'


class FillEventMoneyAction(EventActionAbstract):

    def choose(self) -> FillEventMoneyAction:
        """Choose a value in the arrh radio buttons group."""
        self.page.choose(RADIO_MONEY, self.event.arrh)
        return self
