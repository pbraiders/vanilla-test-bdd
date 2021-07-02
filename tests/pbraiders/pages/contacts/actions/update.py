# coding=utf-8
"""Contact page - update responsability."""

from __future__ import annotations
from pbraiders.pages.contacts.actions import BUTTON_UPDATE
from pbraiders.pages.contacts.actions import MESSAGE_FAILURE
from pbraiders.pages.contacts.actions import MESSAGE_SUCCESS
from pbraiders.pages.contacts.actions import ContactActionAbstract


class ContactUpdateAction(ContactActionAbstract):
    """Contact page - update responsability."""

    def update(self) -> None:
        """Clicks the update button"""
        self.page.find_by_name(BUTTON_UPDATE).first.click()

    def has_failed(self) -> bool:
        """Test if the process has failed"""
        return self.page.is_text_present(MESSAGE_FAILURE, wait_time=1)

    def has_succeeded(self) -> bool:
        """Test if the process has succeded"""
        return self.page.is_text_present(MESSAGE_SUCCESS, wait_time=1)
