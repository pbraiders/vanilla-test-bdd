# coding=utf-8
"""Page Contact - update responsability."""

from __future__ import annotations
from dataclasses import dataclass
from pbraiders.contacts import PageContact

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


@dataclass
class PageContactUpdate(object):
    """Page Contact - update responsability."""
    parent: PageContact

    def is_contact_present(self) -> bool:
        if self.parent.contact is None:
            raise TypeError("Contact is not set!")
        return self.parent.browser.is_element_present_by_value(self.parent.contact.firstname) \
            and self.parent.browser.is_element_present_by_value(self.parent.contact.lastname) \
            and self.parent.browser.is_element_present_by_value(self.parent.contact.tel) \
            and self.parent.browser.is_element_present_by_value(self.parent.contact.email) \
            and self.parent.browser.is_element_present_by_value(self.parent.contact.address) \
            and self.parent.browser.is_element_present_by_value(self.parent.contact.address_more) \
            and self.parent.browser.is_element_present_by_value(self.parent.contact.city) \
            and self.parent.browser.is_element_present_by_value(self.parent.contact.zip)

    def is_contact_comments_present(self) -> bool:
        return self.parent.browser.is_element_present_by_value(self.parent.contact.comment)

    def fill_zip(self) -> PageContactUpdate:
        """Fills the zip field"""
        if self.parent.contact is None:
            raise TypeError("Contact is not set!")
        self.parent.browser.fill(FIELD_ZIP, self.parent.contact.zip)
        return self

    def fill_city(self) -> PageContactUpdate:
        """Fills the city field"""
        if self.parent.contact is None:
            raise TypeError("Contact is not set!")
        self.parent.browser.fill(FIELD_CITY, self.parent.contact.city)
        return self

    def fill_address_more(self) -> PageContactUpdate:
        """Fills the address more field"""
        if self.parent.contact is None:
            raise TypeError("Contact is not set!")
        self.parent.browser.fill(FIELD_ADDRESS_MORE, self.parent.contact.address_more)
        return self

    def fill_address(self) -> PageContactUpdate:
        """Fills the address field"""
        if self.parent.contact is None:
            raise TypeError("Contact is not set!")
        self.parent.browser.fill(FIELD_ADDRESS, self.parent.contact.address)
        return self

    def fill_comment(self) -> PageContactUpdate:
        """Fills the comment field"""
        if self.parent.contact is None:
            raise TypeError("Contact is not set!")
        self.parent.browser.fill(FIELD_COMMENT, self.parent.contact.comment)
        return self

    def fill_email(self) -> PageContactUpdate:
        """Fills the email field"""
        if self.parent.contact is None:
            raise TypeError("Contact is not set!")
        self.parent.browser.fill(FIELD_EMAIL, self.parent.contact.email)
        return self

    def fill_lastname(self) -> PageContactUpdate:
        """Fills the lastname field"""
        if self.parent.contact is None:
            raise TypeError("Contact is not set!")
        self.parent.browser.fill(FIELD_LASTNAME, self.parent.contact.lastname)
        return self

    def fill_firstname(self) -> PageContactUpdate:
        """Fills the firstname field"""
        if self.parent.contact is None:
            raise TypeError("Contact is not set!")
        self.parent.browser.fill(FIELD_FIRSTNAME, self.parent.contact.firstname)
        return self

    def fill_phone(self) -> PageContactUpdate:
        """Fills the phone field"""
        if self.parent.contact is None:
            raise TypeError("Contact is not set!")
        self.parent.browser.fill(FIELD_PHONE, self.parent.contact.tel)
        return self

    def update(self) -> PageContactUpdate:
        """Clicks the update button"""
        self.parent.browser.find_by_name(BUTTON_SEND).first.click()
        return self

    def has_failed(self) -> bool:
        """Test if the process has failed"""
        return self.parent.browser.is_text_present(FAILURE_MESSAGE, wait_time=1)

    def has_succeeded(self) -> bool:
        """Test if the process has succeded"""
        return self.parent.browser.is_text_present(SUCCESS_MESSAGE, wait_time=1)
