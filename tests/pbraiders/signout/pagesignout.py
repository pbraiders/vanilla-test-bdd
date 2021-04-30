# coding=utf-8
"""Sign out page."""

from __future__ import annotations
from urllib.parse import urljoin
from dataclasses import dataclass
from splinter import Browser

TITLE = "PBRaiders - Déconnexion"


@dataclass
class PageSignout(object):
    """Signout page html elements and actions"""
    browser: Browser
    config: dict

    def on_page(self) -> bool:
        """Test if we are on the page"""
        return self.browser.title.lower() == TITLE.lower()

    def visit(self) -> None:
        """Goes to the page"""
        self.browser.visit(urljoin(str(self.config['home']), str(self.config['signout'])))
