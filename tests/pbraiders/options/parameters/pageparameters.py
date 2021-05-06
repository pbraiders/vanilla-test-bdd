# coding=utf-8
"""Parameters page."""

from __future__ import annotations
from urllib.parse import urljoin
from dataclasses import dataclass
from splinter import Browser


TITLE = 'PBRaiders - Paramètres'
HEADER = 'Paramètres'
FIELD_PURGE = 'rey'
FIELD_HEADCOUNT = 'pa{}'
BUTTON_SEND = 'Envoyer'
BUTTON_MODIFY = 'update'
PURGE_FAILURE_MESSAGE = "La date saisie n'est pas valide."
PURGE_SUCCESS_MESSAGE = "Suppression réussie."
HEADCOUNT_FAILURE_MESSAGE = "Une des valeurs n'est pas valide."
HEADCOUNT_SUCCESS_MESSAGE = "Enregistrement réussi."


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

    def update_headcount(self) -> PageParameters:
        """Fills the  max update fields and clicks the button."""
        self.browser.find_by_name(BUTTON_MODIFY).first.click()
        return self

    def headcounts(self) -> PageParameters:
        """Fills the  max update fields."""
        for i_month in range(1, 13, 1):
            self.browser.fill(FIELD_HEADCOUNT.format(i_month), i_month)
        return self

    def check_headcounts(self) -> bool:
        """Checks the headcount fields."""
        b_return = True
        for i_month in range(1, 13, 1):
            i_value = int(self.browser.find_by_name(FIELD_HEADCOUNT.format(i_month)).first.value)
            b_return = (b_return is True) and (i_value == i_month)
        return b_return

    def headcount(self, month: int, value) -> PageParameters:
        """Fills the headcount update field."""
        if 1 <= month <= 12:
            self.browser.fill(FIELD_HEADCOUNT.format(month), value)
        else:
            raise TypeError("month is not valid!")
        return self

    def update_has_failed(self) -> bool:
        """Test if the headcount update has failed"""
        return self.browser.is_text_present(HEADCOUNT_FAILURE_MESSAGE, wait_time=1)

    def update_has_succeeded(self) -> bool:
        """Test if the max update has succeded"""
        return self.browser.is_text_present(HEADCOUNT_SUCCESS_MESSAGE, wait_time=1)
