# coding=utf-8
"""New Contact page - main responsabilities."""

from urllib.parse import urljoin
from pbraiders.pages.contacts import ContactPageAbstract

TITLE = 'PBRaiders - Nouveau contact'
HEADER = 'Nouveau contact'


class ContactNewPage(ContactPageAbstract):
    """New Contact page - main responsabilities."""

    def on_page(self) -> bool:
        """Returns True if we are visiting this page."""
        return self.page.title.lower() == TITLE.lower() and self.page.find_by_tag('h1').first.text.lower() == HEADER.lower()

    def visit(self) -> bool:
        """Goes to the page"""
        self.page.visit(urljoin(str(self.config['home']), str(self.config['contact-new'])))
        return self.on_page()
