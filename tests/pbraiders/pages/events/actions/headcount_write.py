# coding=utf-8
"""Event page - fill fields responsability."""

from __future__ import annotations
from pbraiders.pages.events.actions import FIELD_REAL
from pbraiders.pages.events.actions import FIELD_PLANNED
from pbraiders.pages.events.actions import FIELD_CANCELED
from pbraiders.pages.events.actions import FIELD_MAX
from pbraiders.pages.events.actions import EventActionAbstract


class EventHeadcountWriteAction(EventActionAbstract):

    def fill_real(self) -> EventHeadcountWriteAction:
        """Fills the zip field"""
        self.page.fill(FIELD_REAL, self.event.headcount.real)
        return self

    def fill_planned(self) -> EventHeadcountWriteAction:
        """Fills the city field"""
        self.page.fill(FIELD_PLANNED, self.event.headcount.planned)
        return self

    def fill_canceled(self) -> EventHeadcountWriteAction:
        """Fills the zip field"""
        self.page.fill(FIELD_CANCELED, self.event.headcount.canceled)
        return self

    def fill_max(self) -> EventHeadcountWriteAction:
        """Fills the city field"""
        self.page.fill(FIELD_MAX, self.event.headcount.max)
        return self
