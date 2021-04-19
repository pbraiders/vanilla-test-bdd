# coding=utf-8
"""Parameters page."""

from dataclasses import dataclass
from splinter import Browser
from urllib.parse import urljoin


@dataclass
class PageParameters:
    browser: Browser
    config: dict

    # locators
    _TITLE = 'PBRaiders - Paramètres'
    _LINK_OPTIONS = 'Options'

    def goTo(self):
        self.browser.click_link_by_text(self._LINK_OPTIONS)
        assert self.browser.title == self._TITLE
        return self
