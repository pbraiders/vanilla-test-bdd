# coding=utf-8
"""Event page - fill fields responsability."""

from __future__ import annotations
from pbraiders.pages.events.actions import EventActionAbstract

FIELD_REAL = 'rer'
FIELD_PLANNED = 'rep'
FIELD_CANCELED = 'rec'
FIELD_MAX = 'max'


class FillEventHeadcountAction(EventActionAbstract):

    def fill_real(self) -> FillEventHeadcountAction:
        """Fills the zip field"""
        self.page.fill(FIELD_REAL, self.event.headcount.real)
        return self

    def fill_planned(self) -> FillEventHeadcountAction:
        """Fills the city field"""
        self.page.fill(FIELD_PLANNED, self.event.headcount.planned)
        return self

    def fill_canceled(self) -> FillEventHeadcountAction:
        """Fills the zip field"""
        self.page.fill(FIELD_CANCELED, self.event.headcount.canceled)
        return self

    def fill_max(self) -> FillEventHeadcountAction:
        """Fills the city field"""
        self.page.fill(FIELD_MAX, self.event.headcount.max)
        return self
