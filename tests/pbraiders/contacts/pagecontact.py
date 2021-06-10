# coding=utf-8
"""contact page."""

from __future__ import annotations
from typing import Optional
from urllib.parse import urljoin
from dataclasses import dataclass
from splinter import Browser
from pbraiders.contact import Contact

TITLE = 'PBRaiders - {lastname} {firstname}'
HEADER = '{lastname} {firstname}'
FIELD_LASTNAME = 'ctl'
FIELD_FIRSTNAME = 'ctf'
FIELD_PHONE = 'ctp'
FIELD_EMAIL = 'cte'
FIELD_ADDRESS = 'cta'
FIELD_ADDRESS_MORE = 'ctm'
FIELD_CITY = 'ctc'
FIELD_ZIP = 'ctz'
FIELD_COMMENT = 'ctk'
BUTTON_SEND = 'upd'
FAILURE_MESSAGE = "Le nom,le prénom et le numéro de téléphone doivent être renseignés."
SUCCESS_MESSAGE = "Enregistrement réussi."
CONTACT_LIST_LOCATOR = "//*[contains(text(),'{lastname} {firstname} • {phone}')]/.."


@dataclass
class PageContact(object):
    """Contact page html elements and actions"""
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
        self.browser.visit(urljoin(str(self.config['home']), str(self.config['contacts'])))
        try:
            self.browser.find_by_xpath(CONTACT_LIST_LOCATOR.format(lastname=self.contact.lastname,
                                       firstname=self.contact.firstname, phone=self.contact.tel)).first.click()
        except Exception:
            pass
        return self.on_page()

    def is_contact_present(self) -> bool:
        return self.browser.is_element_present_by_value(self.contact.firstname) \
            and self.browser.is_element_present_by_value(self.contact.lastname) \
            and self.browser.is_element_present_by_value(self.contact.tel) \
            and self.browser.is_element_present_by_value(self.contact.email) \
            and self.browser.is_element_present_by_value(self.contact.address) \
            and self.browser.is_element_present_by_value(self.contact.address_more) \
            and self.browser.is_element_present_by_value(self.contact.city) \
            and self.browser.is_element_present_by_value(self.contact.zip)

    def is_contact_comments_present(self) -> bool:
        return self.browser.is_element_present_by_value(self.contact.comment)

    def fill_zip(self) -> PageContact:
        """Fills the zip field"""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        self.browser.fill(FIELD_ZIP, self.contact.zip)
        return self

    def fill_city(self) -> PageContact:
        """Fills the city field"""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        self.browser.fill(FIELD_CITY, self.contact.city)
        return self

    def fill_address_more(self) -> PageContact:
        """Fills the address more field"""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        self.browser.fill(FIELD_ADDRESS_MORE, self.contact.address_more)
        return self

    def fill_address(self) -> PageContact:
        """Fills the address field"""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        self.browser.fill(FIELD_ADDRESS, self.contact.address)
        return self

    def fill_email(self) -> PageContact:
        """Fills the email field"""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        self.browser.fill(FIELD_EMAIL, self.contact.email)
        return self

    def fill_lastname(self) -> PageContact:
        """Fills the lastname field"""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        self.browser.fill(FIELD_LASTNAME, self.contact.lastname)
        return self

    def fill_firstname(self) -> PageContact:
        """Fills the firstname field"""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        self.browser.fill(FIELD_FIRSTNAME, self.contact.firstname)
        return self

    def fill_phone(self) -> PageContact:
        """Fills the phone field"""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        self.browser.fill(FIELD_PHONE, self.contact.tel)
        return self

    def click(self) -> PageContact:
        """Clicks the button"""
        self.browser.find_by_name(BUTTON_SEND).first.click()
        return self

    def has_failed(self) -> bool:
        """Test if the process has failed"""
        return self.browser.is_text_present(FAILURE_MESSAGE, wait_time=1)

    def has_succeeded(self) -> bool:
        """Test if the process has succeded"""
        return self.browser.is_text_present(SUCCESS_MESSAGE, wait_time=1)
