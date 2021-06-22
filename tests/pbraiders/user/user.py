# coding=utf-8
"""User requesting a web page."""

from dataclasses import dataclass


@dataclass
class User(object):
    """User requesting a web page."""

    login: str = ''
    password: str = ''
    passwordc: str = ''

    def dump(self, obj):
        for attr in dir(obj):
            if hasattr(obj, attr):
                print("obj.%s = %s" % (attr, getattr(obj, attr)))
