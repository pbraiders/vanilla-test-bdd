# coding=utf-8
"""Page Contact - delete responsability."""

from __future__ import annotations
from dataclasses import dataclass
from pbraiders.contacts import PageContact

BUTTON_DELETE = 'del'
SUCCESS_MESSAGE = "Enregistrement réussi."


@dataclass
class PageContactDelete(object):
    """Page Contact - delete responsability."""
    parent: PageContact

    def delete(self) -> PageContactDelete:
        """Clicks the delete button"""
        self.parent.browser.find_by_name(BUTTON_DELETE).first.click()
        return self

    def has_succeeded(self) -> bool:
        """Test if the process has succeded"""
        return self.parent.browser.is_text_present(SUCCESS_MESSAGE, wait_time=1)
