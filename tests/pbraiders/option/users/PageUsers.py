# coding=utf-8
"""Users page."""

from dataclasses import dataclass
from splinter import Browser
from urllib.parse import urljoin


@dataclass
class PageUsers:
    browser: Browser
    config: dict

    # locators
    _TITLE = 'PBRaiders - Utilisateurs'
    _LINK_USERS = 'Utilisateurs'

    def goTo(self):
        self.browser.visit(urljoin(str(self.config['home']), str(self.config['users'])))
        # self.browser.click_link_by_text(self._LINK_USERS)
        assert self.browser.title == self._TITLE
        return self
