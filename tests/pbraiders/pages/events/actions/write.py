# coding=utf-8
"""Event page - fill fields responsability."""

from __future__ import annotations
from pbraiders.pages.events.actions import FIELD_COMMENT
from pbraiders.pages.events.actions import EventActionAbstract


class EventWriteAction(EventActionAbstract):

    def fill_comment(self) -> None:
        """Fills the comment field"""
        self.page.fill(FIELD_COMMENT, self.event.comment)
