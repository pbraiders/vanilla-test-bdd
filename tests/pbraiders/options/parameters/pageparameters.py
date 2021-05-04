# coding=utf-8
"""Parameters page."""

from __future__ import annotations
from urllib.parse import urljoin
from dataclasses import dataclass
from splinter import Browser


TITLE = 'PBRaiders - Paramètres'
HEADER = 'Paramètres'
FIELD_PURGE = 'rey'
BUTTON_SEND = 'Envoyer'
PURGE_FAILURE_MESSAGE = "La date saisie n'est pas valide."
PURGE_SUCCESS_MESSAGE = "Suppression réussie."


@dataclass
class PageParameters(object):
    """Parameters page html elements and actions"""
    browser: Browser
    config: dict

    def on_page(self) -> bool:
        """Test if we are on the page"""
        return self.browser.title.lower() == TITLE.lower() and self.browser.find_by_tag('h1').first.text.lower() == HEADER.lower()

    def visit(self) -> bool:
        """Goes to the parameters page"""
        self.browser.visit(
            urljoin(str(self.config['home']), str(self.config['parameters'])))
        return self.on_page()

    def purge(self, value: str = None) -> PageParameters:
        """Fills the purge field and clicks the button."""
        if value is not None:
            self.browser.fill(FIELD_PURGE, int(value))
        self.browser.find_by_value(BUTTON_SEND).first.click()
        return self

    def purge_has_failed(self) -> bool:
        """Test if the purge has failed"""
        return self.browser.is_text_present(PURGE_FAILURE_MESSAGE, wait_time=1)

    def purge_has_succeeded(self) -> bool:
        """Test if the purge has succeded"""
        return self.browser.is_text_present(PURGE_SUCCESS_MESSAGE, wait_time=1)
