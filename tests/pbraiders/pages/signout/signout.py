# coding=utf-8
"""Sign-out page."""

from __future__ import annotations
from urllib.parse import urljoin
from pbraiders.pages import PageAbstract

TITLE = "PBRaiders - Déconnexion"


class SignoutPage(PageAbstract):
    """Sign-out page."""

    def on_page(self) -> bool:
        """Returns True if we are visiting this page."""
        return self.page.title.lower() == TITLE.lower()

    def visit(self) -> bool:
        """Goes to the page"""
        self.page.visit(urljoin(str(self.config['home']), str(self.config['signout'])))
        return self.on_page()
