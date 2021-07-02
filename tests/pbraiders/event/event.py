# coding=utf-8
"""Event."""

from __future__ import annotations
from dataclasses import dataclass

from pbraiders.event import Date
from pbraiders.event import Headcount


@dataclass
class Event(object):
    """Event."""
    date: Date
    headcount: Headcount
    age: str = ''
    arrh: str = ''
    comment: str = ''

    def dump(self, obj):
        for attr in dir(obj):
            if hasattr(obj, attr):
                print("obj.%s = %s" % (attr, getattr(obj, attr)))
