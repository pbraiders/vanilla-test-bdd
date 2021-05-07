# coding=utf-8
"""Parameters page."""

from __future__ import annotations
from dataclasses import dataclass
from splinter import Browser


TITLE = 'PBRaiders - Supprimer les anciennes réservations'
HEADER = 'Supprimer les anciennes réservations'
MESSAGE = 'Toutes les réservations antérieures à {0} vont être supprimées'
BUTTON_CONFIRM = 'con'
BUTTON_CANCEL = 'can'


@dataclass
class PagePurge(object):
    """Parameters page html elements and actions"""
    browser: Browser
    year: str

    def on_page(self) -> bool:
        """Test if we are on the page"""
        return self.browser.is_text_present(MESSAGE.format(self.year))

    def cancel(self) -> None:
        """Cancel the deletion."""
        self.browser.find_by_name(BUTTON_CANCEL).first.click()

    def confirm(self) -> None:
        """Confirm the deletion."""
        self.browser.find_by_name(BUTTON_CONFIRM).first.click()
