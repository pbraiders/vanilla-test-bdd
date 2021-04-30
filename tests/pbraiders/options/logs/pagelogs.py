# coding=utf-8
"""Logs page."""

from __future__ import annotations
from urllib.parse import urljoin
from dataclasses import dataclass
from splinter import Browser


TITLE = 'PBRaiders - Logs'


@dataclass
class PageLogs(object):
    """Logs page html elements and actions"""
    browser: Browser
    config: dict

    def on_page(self) -> bool:
        """Test if we already are on the page"""
        return self.browser.title.lower() == TITLE.lower()

    def visit(self) -> bool:
        """Goes to the logs page"""
        self.browser.visit(
            urljoin(str(self.config['home']), str(self.config['logs'])))
        return self.on_page()
