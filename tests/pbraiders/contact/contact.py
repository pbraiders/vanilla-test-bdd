# coding=utf-8
"""Contact."""

from dataclasses import dataclass


@dataclass
class Contact(object):
    """Contact."""
    lastname: str = ''
    firstname: str = ''
    tel: str = ''
    email: str = ''
    address: str = ''
    address_more: str = ''
    city: str = ''
    zip: str = ''
    comment: str = ''

    def dump(self, obj):
        for attr in dir(obj):
            if hasattr(obj, attr):
                print("obj.%s = %s" % (attr, getattr(obj, attr)))
