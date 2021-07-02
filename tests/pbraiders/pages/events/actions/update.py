# coding=utf-8
"""Event page - update responsability."""

from __future__ import annotations
from pbraiders.pages.events.actions import MESSAGE_SUCCESS
from pbraiders.pages.events.actions import BUTTON_UPDATE
from pbraiders.pages.events.actions import EventActionAbstract


class EventUpdateAction(EventActionAbstract):
    """Event page - update responsability."""

    def update(self) -> None:
        """Clicks the button"""
        self.page.find_by_name(BUTTON_UPDATE).first.click()

    def has_succeeded(self) -> bool:
        """Test if the process has succeded"""
        return self.page.is_text_present(MESSAGE_SUCCESS, wait_time=1)
