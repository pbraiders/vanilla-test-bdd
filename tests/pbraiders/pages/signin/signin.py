# coding=utf-8
"""Sign-in page - main responsabilities."""

from __future__ import annotations
from urllib.parse import urljoin
from pbraiders.pages.signin import SigninPageAbstract

TITLE = "PBRaiders - Connexion"


class SigninPage(SigninPageAbstract):
    """Sign-in page - main responsabilities."""

    def on_page(self) -> bool:
        """Returns True if we are visiting this page."""
        return self.page.title.lower() == TITLE.lower()

    def visit(self) -> bool:
        """Goes to the page"""
        self.page.visit(urljoin(str(self.config['home']), str(self.config['signin'])))
        return self.on_page()

    def sign_out(self) -> SigninPage:
        """Goes to the sign out page"""
        self.page.visit(urljoin(str(self.config['home']), str(self.config['signout'])))
        return self
