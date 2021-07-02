# coding=utf-8
"""Headcount."""

from dataclasses import dataclass


@dataclass
class Headcount(object):
    """Headcount."""
    real: str = ''
    planned: str = ''
    canceled: str = ''
    max: str = ''

    def dump(self, obj):
        for attr in dir(obj):
            if hasattr(obj, attr):
                print("obj.%s = %s" % (attr, getattr(obj, attr)))
