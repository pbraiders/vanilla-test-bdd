# coding=utf-8
"""Headcount."""

import calendar
from dataclasses import dataclass
from datetime import date


@dataclass
class Date(object):
    """Date."""
    _year: int = date.today().year
    _month: int = date.today().month
    _day: int = date.today().day

    def date_name(self) -> str:
        """Returns month name with year."""
        p_calendar = calendar.LocaleTextCalendar(locale=('fr', 'UTF-8'))
        s_return = '{day} {month}'.format(day=self._day, month=p_calendar.formatmonthname(
            theyear=self._year, themonth=self._month, width=0, withyear=True))
        return s_return

    def dump(self, obj):
        for attr in dir(obj):
            if hasattr(obj, attr):
                print("obj.%s = %s" % (attr, getattr(obj, attr)))
