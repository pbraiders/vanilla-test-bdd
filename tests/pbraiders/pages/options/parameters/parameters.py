# coding=utf-8
"""Parameters page - main responsabilities."""

from urllib.parse import urljoin
from pbraiders.pages import PageAbstract

TITLE = 'PBRaiders - Paramètres'
HEADER = 'Paramètres'


class ParametersPage(PageAbstract):
    """Parameters page - main responsabilities."""

    def on_page(self) -> bool:
        """Returns True if we are visiting this page."""
        return self.page.title.lower() == TITLE.lower() and self.page.find_by_tag('h1').first.text.lower() == HEADER.lower()

    def visit(self) -> bool:
        """Goes to the parameters page"""
        self.page.visit(
            urljoin(str(self.config['home']), str(self.config['parameters'])))
        return self.on_page()
