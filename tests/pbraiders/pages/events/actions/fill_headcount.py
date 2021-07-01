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

    def is_valid_real(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_REAL)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value) == str(self.event.headcount.real)

    def fill_planned(self) -> FillEventHeadcountAction:
        """Fills the city field"""
        self.page.fill(FIELD_PLANNED, self.event.headcount.planned)
        return self

    def is_valid_planned(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_PLANNED)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value) == str(self.event.headcount.planned)

    def fill_canceled(self) -> FillEventHeadcountAction:
        """Fills the zip field"""
        self.page.fill(FIELD_CANCELED, self.event.headcount.canceled)
        return self

    def is_valid_canceled(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_CANCELED)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value) == str(self.event.headcount.canceled)

    def fill_max(self) -> FillEventHeadcountAction:
        """Fills the city field"""
        self.page.fill(FIELD_MAX, self.event.headcount.max)
        return self

    def is_valid_max(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_MAX)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value) == str(self.event.headcount.max)
