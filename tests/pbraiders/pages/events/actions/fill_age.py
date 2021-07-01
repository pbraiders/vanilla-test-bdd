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
