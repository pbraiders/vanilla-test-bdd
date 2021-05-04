# coding=utf-8
"""Graphs page."""

from __future__ import annotations
from urllib.parse import urljoin
from dataclasses import dataclass
from splinter import Browser


TITLE = 'PBRaiders - Graphes'


@dataclass
class PageGraphs(object):
    """Graphs page html elements and actions"""
    browser: Browser
    config: dict

    def on_page(self) -> bool:
        """Test if we are on the page"""
        return self.browser.title.lower().find(TITLE.lower()) >= 0

    def visit(self) -> bool:
        """Goes to the graphs page"""
        self.browser.visit(
            urljoin(str(self.config['home']), str(self.config['graphs'])))
        return self.on_page()
