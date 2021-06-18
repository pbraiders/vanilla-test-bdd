# coding=utf-8
"""Contact page - fill fields responsability."""

from __future__ import annotations
from pbraiders.pages.contacts.actions import ContactActionAbstract

FIELD_LASTNAME = 'ctl'
FIELD_FIRSTNAME = 'ctf'
FIELD_PHONE = 'ctp'
FIELD_EMAIL = 'cte'
FIELD_ADDRESS = 'cta'
FIELD_ADDRESS_MORE = 'ctm'
FIELD_CITY = 'ctc'
FIELD_ZIP = 'ctz'
FIELD_COMMENT = 'ctk'


class FillContactAction(ContactActionAbstract):

    def fill_zip(self) -> FillContactAction:
        """Fills the zip field"""
        self.page.fill(FIELD_ZIP, self.contact.zip)
        return self

    def fill_city(self) -> FillContactAction:
        """Fills the city field"""
        self.page.fill(FIELD_CITY, self.contact.city)
        return self

    def fill_address_more(self) -> FillContactAction:
        """Fills the address more field"""
        self.page.fill(FIELD_ADDRESS_MORE, self.contact.address_more)
        return self

    def fill_address(self) -> FillContactAction:
        """Fills the address field"""
        self.page.fill(FIELD_ADDRESS, self.contact.address)
        return self

    def fill_comment(self) -> FillContactAction:
        """Fills the comment field"""
        self.page.fill(FIELD_COMMENT, self.contact.comment)
        return self

    def fill_email(self) -> FillContactAction:
        """Fills the email field"""
        self.page.fill(FIELD_EMAIL, self.contact.email)
        return self

    def fill_lastname(self) -> FillContactAction:
        """Fills the lastname field"""
        self.page.fill(FIELD_LASTNAME, self.contact.lastname)
        return self

    def fill_firstname(self) -> FillContactAction:
        """Fills the firstname field"""
        self.page.fill(FIELD_FIRSTNAME, self.contact.firstname)
        return self

    def fill_phone(self) -> FillContactAction:
        """Fills the phone field"""
        self.page.fill(FIELD_PHONE, self.contact.tel)
        return self
