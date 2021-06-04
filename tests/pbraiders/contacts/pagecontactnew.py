# coding=utf-8
"""New contact page."""

from __future__ import annotations
from typing import Optional
from urllib.parse import urljoin
from dataclasses import dataclass
from splinter import Browser
from pbraiders.contact import Contact

TITLE = 'PBRaiders - Nouveau contact'
HEADER = 'Nouveau contact'
FIELD_LASTNAME = 'ctl'
FIELD_FIRSTNAME = 'ctf'
FIELD_PHONE = 'ctp'
FIELD_EMAIL = 'cte'
FIELD_ADDRESS = 'cta'
FIELD_ADDRESS_MORE = 'ctm'
FIELD_CITY = 'ctc'
FIELD_ZIP = 'ctz'
BUTTON_SEND = 'new'
FAILURE_MESSAGE = "le nom,le prénom et le numéro de téléphone doivent être renseignés."
SUCCESS_MESSAGE = "Enregistrement réussi."


@dataclass
class PageContactNew(object):
    """New contact page html elements and actions"""
    browser: Browser
    config: dict
    contact: Optional[Contact] = None

    def set_contact(self, contact: Contact = None) -> PageContactNew:
        """Contact setter"""
        self.contact = contact
        return self

    def on_page(self) -> bool:
        """Test if we already are on the page"""
        return self.browser.title.lower() == TITLE.lower() and self.browser.find_by_tag('h1').first.text.lower() == HEADER.lower()

    def visit(self) -> bool:
        """Goes to the page"""
        self.browser.visit(urljoin(str(self.config['home']), str(self.config['contact-new'])))
        return self.on_page()

    def fill_zip(self) -> PageContactNew:
        """Fills the zip field"""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        self.browser.fill(FIELD_ZIP, self.contact.zip)
        return self

    def fill_city(self) -> PageContactNew:
        """Fills the city field"""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        self.browser.fill(FIELD_CITY, self.contact.city)
        return self

    def fill_address_more(self) -> PageContactNew:
        """Fills the address more field"""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        self.browser.fill(FIELD_ADDRESS_MORE, self.contact.address_more)
        return self

    def fill_address(self) -> PageContactNew:
        """Fills the address field"""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        self.browser.fill(FIELD_ADDRESS, self.contact.address)
        return self

    def fill_email(self) -> PageContactNew:
        """Fills the email field"""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        self.browser.fill(FIELD_EMAIL, self.contact.email)
        return self

    def fill_lastname(self) -> PageContactNew:
        """Fills the lastname field"""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        self.browser.fill(FIELD_LASTNAME, self.contact.lastname)
        return self

    def fill_firstname(self) -> PageContactNew:
        """Fills the firstname field"""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        self.browser.fill(FIELD_FIRSTNAME, self.contact.firstname)
        return self

    def fill_phone(self) -> PageContactNew:
        """Fills the phone field"""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        self.browser.fill(FIELD_PHONE, self.contact.tel)
        return self

    def click(self) -> PageContactNew:
        """Clicks the button"""
        self.browser.find_by_name(BUTTON_SEND).first.click()
        return self

    def has_failed(self) -> bool:
        """Test if the process has failed"""
        return self.browser.is_text_present(FAILURE_MESSAGE, wait_time=1)

    def has_succeeded(self) -> bool:
        """Test if the process has succeded"""
        return self.browser.is_text_present(SUCCESS_MESSAGE, wait_time=1)
