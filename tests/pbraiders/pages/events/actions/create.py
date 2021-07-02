# coding=utf-8
"""Event page - creation responsability."""

from __future__ import annotations
from pbraiders.pages.events.actions import MESSAGE_FAILURE
from pbraiders.pages.events.actions import MESSAGE_SUCCESS
from pbraiders.pages.events.actions import BUTTON_CREATE
from pbraiders.pages.events.actions import EventActionAbstract


class EventCreateAction(EventActionAbstract):
    """Event page - creation responsability."""

    def click(self) -> None:
        """Clicks the button"""
        self.page.find_by_name(BUTTON_CREATE).first.click()

    def has_failed(self) -> bool:
        """Test if the process has failed"""
        return self.page.is_text_present(MESSAGE_FAILURE, wait_time=1)

    def has_succeeded(self) -> bool:
        """Test if the process has succeded"""
        return self.page.is_text_present(MESSAGE_SUCCESS, wait_time=1)
