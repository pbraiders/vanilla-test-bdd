# coding=utf-8
"""Event page - choose age radio button responsability."""

from __future__ import annotations
from pbraiders.pages.events.actions import EventActionAbstract

RADIO_AGE = 'rea'


class FillEventAgeAction(EventActionAbstract):

    def choose(self) -> FillEventAgeAction:
        """Choose a value in the age radio buttons group."""
        self.page.choose(RADIO_AGE, self.event.age)
        return self

    def is_valid(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(RADIO_AGE)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value) == str(self.event.age)
