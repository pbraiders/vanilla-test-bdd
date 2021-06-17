# coding=utf-8
"""New Contact page - main responsabilities."""

from urllib.parse import urljoin
from pbraiders.contacts import ContactPageAbstract

TITLE = 'PBRaiders - Nouveau contact'
HEADER = 'Nouveau contact'


class ContactNewPage(ContactPageAbstract):
    """New Contact page - main responsabilities."""

    def on_page(self) -> bool:
        """Test if we already are on the page"""
        return self.browser.title.lower() == TITLE.lower() and self.browser.find_by_tag('h1').first.text.lower() == HEADER.lower()

    def visit(self) -> bool:
        """Goes to the page"""
        self.browser.visit(urljoin(str(self.config['home']), str(self.config['contact-new'])))
        return self.on_page()
