# coding=utf-8
"""Contact page - main responsabilities."""

from __future__ import annotations
from typing import Optional
from urllib.parse import urljoin
from dataclasses import dataclass
from splinter import Browser
from pbraiders.contact import Contact

TITLE = 'PBRaiders - {lastname} {firstname}'
HEADER = '{lastname} {firstname}'
CONTACT_LIST_LOCATOR = "//*[contains(text(),'{lastname} {firstname} • {phone}')]/.."


@dataclass
class PageContact(object):
    """Contact page - main responsabilities."""
    browser: Browser
    config: dict
    contact: Optional[Contact] = None

    def set_contact(self, contact: Contact = None) -> PageContact:
        """Contact setter"""
        self.contact = contact
        return self

    def on_page(self) -> bool:
        """Test if we already are on the page"""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        s_title = TITLE.format(lastname=self.contact.lastname, firstname=self.contact.firstname)
        s_header = HEADER.format(lastname=self.contact.lastname, firstname=self.contact.firstname)
        return (self.browser.title.lower() == s_title.lower()) and (self.browser.find_by_tag('h1').first.text.lower() == s_header.lower())

    def visit(self) -> bool:
        """Goes to the page."""
        if self.contact is None:
            raise TypeError("User is not set!")
        try:
            self.browser.visit(urljoin(str(self.config['home']), str(self.config['contacts'])))
            self.browser.find_by_xpath(CONTACT_LIST_LOCATOR.format(lastname=self.contact.lastname,
                                       firstname=self.contact.firstname, phone=self.contact.tel)).first.click()
        except Exception:
            pass
        return self.on_page()
