# coding=utf-8
"""Page Contact - fill fields responsability."""

from __future__ import annotations
from pbraiders.contacts import ActionContactAbstract

FIELD_LASTNAME = 'ctl'
FIELD_FIRSTNAME = 'ctf'
FIELD_PHONE = 'ctp'
FIELD_EMAIL = 'cte'
FIELD_ADDRESS = 'cta'
FIELD_ADDRESS_MORE = 'ctm'
FIELD_CITY = 'ctc'
FIELD_ZIP = 'ctz'
FIELD_COMMENT = 'ctk'


class ActionContactFill(ActionContactAbstract):

    def fill_zip(self) -> ActionContactFill:
        """Fills the zip field"""
        self.browser.fill(FIELD_ZIP, self.contact.zip)
        return self

    def fill_city(self) -> ActionContactFill:
        """Fills the city field"""
        self.browser.fill(FIELD_CITY, self.contact.city)
        return self

    def fill_address_more(self) -> ActionContactFill:
        """Fills the address more field"""
        self.browser.fill(FIELD_ADDRESS_MORE, self.contact.address_more)
        return self

    def fill_address(self) -> ActionContactFill:
        """Fills the address field"""
        self.browser.fill(FIELD_ADDRESS, self.contact.address)
        return self

    def fill_comment(self) -> ActionContactFill:
        """Fills the comment field"""
        self.browser.fill(FIELD_COMMENT, self.contact.comment)
        return self

    def fill_email(self) -> ActionContactFill:
        """Fills the email field"""
        self.browser.fill(FIELD_EMAIL, self.contact.email)
        return self

    def fill_lastname(self) -> ActionContactFill:
        """Fills the lastname field"""
        self.browser.fill(FIELD_LASTNAME, self.contact.lastname)
        return self

    def fill_firstname(self) -> ActionContactFill:
        """Fills the firstname field"""
        self.browser.fill(FIELD_FIRSTNAME, self.contact.firstname)
        return self

    def fill_phone(self) -> ActionContactFill:
        """Fills the phone field"""
        self.browser.fill(FIELD_PHONE, self.contact.tel)
        return self
