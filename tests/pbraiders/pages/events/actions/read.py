# coding=utf-8
"""Event page - fill fields responsability."""

from __future__ import annotations
from pbraiders.pages.events.actions import FIELD_COMMENT
from pbraiders.pages.events.actions import EventActionAbstract


class EventReadAction(EventActionAbstract):

    def is_equal_comment(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_COMMENT)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value).lower() == str(self.event.comment).lower()
