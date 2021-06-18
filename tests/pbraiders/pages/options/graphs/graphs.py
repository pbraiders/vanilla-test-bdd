# coding=utf-8
"""Graphs page - main responsabilities."""

from urllib.parse import urljoin
from pbraiders.pages import PageAbstract

TITLE = 'PBRaiders - Graphes'


class GraphsPage(PageAbstract):
    """Graphs page - main responsabilities."""

    def on_page(self) -> bool:
        """Returns True if we are visiting this page."""
        return self.page.title.lower().find(TITLE.lower()) >= 0

    def visit(self) -> bool:
        """Goes to the graphs page"""
        self.page.visit(urljoin(str(self.config['home']), str(self.config['graphs'])))
        return self.on_page()
