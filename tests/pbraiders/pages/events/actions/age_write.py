# coding=utf-8
"""Event page - choose age radio button responsability."""

from __future__ import annotations
from pbraiders.pages.events.actions import RADIO_AGE
from pbraiders.pages.events.actions import EventActionAbstract


class EventAgeWriteAction(EventActionAbstract):

    def choose(self) -> None:
        """Choose a value in the age radio buttons group."""
        self.page.choose(RADIO_AGE, self.event.age)
