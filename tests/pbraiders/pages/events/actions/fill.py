# coding=utf-8
"""Event page - fill fields responsability."""

from __future__ import annotations
from pbraiders.pages.events.actions import EventActionAbstract

FIELD_LASTNAME = 'ctl'
FIELD_FIRSTNAME = 'ctf'
FIELD_PHONE = 'ctp'
FIELD_EMAIL = 'cte'
FIELD_ADDRESS = 'cta'
FIELD_ADDRESS_MORE = 'ctm'
FIELD_CITY = 'ctc'
FIELD_ZIP = 'ctz'


class FillEventAction(EventActionAbstract):

    def fill_zip(self) -> FillEventAction:
        """Fills the zip field"""
        self.page.fill(FIELD_ZIP, self.contact.zip)
        return self

    def fill_city(self) -> FillEventAction:
        """Fills the city field"""
        self.page.fill(FIELD_CITY, self.contact.city)
        return self

    def fill_address_more(self) -> FillEventAction:
        """Fills the address more field"""
        self.page.fill(FIELD_ADDRESS_MORE, self.contact.address_more)
        return self

    def fill_address(self) -> FillEventAction:
        """Fills the address field"""
        self.page.fill(FIELD_ADDRESS, self.contact.address)
        return self

    def fill_email(self) -> FillEventAction:
        """Fills the email field"""
        self.page.fill(FIELD_EMAIL, self.contact.email)
        return self

    def fill_lastname(self) -> FillEventAction:
        """Fills the lastname field"""
        self.page.fill(FIELD_LASTNAME, self.contact.lastname)
        return self

    def fill_firstname(self) -> FillEventAction:
        """Fills the firstname field"""
        self.page.fill(FIELD_FIRSTNAME, self.contact.firstname)
        return self

    def fill_phone(self) -> FillEventAction:
        """Fills the phone field"""
        self.page.fill(FIELD_PHONE, self.contact.tel)
        return self
