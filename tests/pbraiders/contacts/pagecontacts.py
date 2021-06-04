# coding=utf-8
"""New contact page."""

from __future__ import annotations
from urllib.parse import urljoin
from dataclasses import dataclass
from splinter import Browser

TITLE = 'PBRaiders - Contacts'
HEADER = 'Contacts'


@dataclass
class PageContacts(object):
    """New contact page html elements and actions"""
    browser: Browser
    config: dict

    def on_page(self) -> bool:
        """Test if we already are on the page"""
        return self.browser.title.lower() == TITLE.lower() and self.browser.find_by_tag('h1').first.text.lower() == HEADER.lower()

    def visit(self) -> bool:
        """Goes to the page"""
        self.browser.visit(urljoin(str(self.config['home']), str(self.config['contacts'])))
        return self.on_page()
