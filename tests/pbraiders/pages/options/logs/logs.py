# coding=utf-8
"""Logs page - main responsabilities."""

from urllib.parse import urljoin
from pbraiders.pages import PageAbstract


TITLE = 'PBRaiders - Logs'


class LogsPage(PageAbstract):
    """Logs page - main responsabilities."""

    def on_page(self) -> bool:
        """Returns True if we are visiting this page."""
        return self.page.title.lower() == TITLE.lower()

    def visit(self) -> bool:
        """Goes to the logs page"""
        self.page.visit(urljoin(str(self.config['home']), str(self.config['logs'])))
        return self.on_page()
