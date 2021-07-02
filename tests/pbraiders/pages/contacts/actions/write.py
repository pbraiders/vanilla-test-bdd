# coding=utf-8
"""Contact page - fill fields responsability."""

from __future__ import annotations
from pbraiders.pages.contacts.actions import FIELD_LASTNAME
from pbraiders.pages.contacts.actions import FIELD_FIRSTNAME
from pbraiders.pages.contacts.actions import FIELD_PHONE
from pbraiders.pages.contacts.actions import FIELD_EMAIL
from pbraiders.pages.contacts.actions import FIELD_ADDRESS
from pbraiders.pages.contacts.actions import FIELD_ADDRESS_MORE
from pbraiders.pages.contacts.actions import FIELD_CITY
from pbraiders.pages.contacts.actions import FIELD_ZIP
from pbraiders.pages.contacts.actions import FIELD_COMMENT
from pbraiders.pages.contacts.actions import ContactActionAbstract


class ContactWriteAction(ContactActionAbstract):

    def fill_zip(self) -> ContactWriteAction:
        """Fills the zip field"""
        self.page.fill(FIELD_ZIP, self.contact.zip)
        return self

    def fill_city(self) -> ContactWriteAction:
        """Fills the city field"""
        self.page.fill(FIELD_CITY, self.contact.city)
        return self

    def fill_address_more(self) -> ContactWriteAction:
        """Fills the address more field"""
        self.page.fill(FIELD_ADDRESS_MORE, self.contact.address_more)
        return self

    def fill_address(self) -> ContactWriteAction:
        """Fills the address field"""
        self.page.fill(FIELD_ADDRESS, self.contact.address)
        return self

    def fill_comment(self) -> ContactWriteAction:
        """Fills the comment field"""
        self.page.fill(FIELD_COMMENT, self.contact.comment)
        return self

    def fill_email(self) -> ContactWriteAction:
        """Fills the email field"""
        self.page.fill(FIELD_EMAIL, self.contact.email)
        return self

    def fill_lastname(self) -> ContactWriteAction:
        """Fills the lastname field"""
        self.page.fill(FIELD_LASTNAME, self.contact.lastname)
        return self

    def fill_firstname(self) -> ContactWriteAction:
        """Fills the firstname field"""
        self.page.fill(FIELD_FIRSTNAME, self.contact.firstname)
        return self

    def fill_phone(self) -> ContactWriteAction:
        """Fills the phone field"""
        self.page.fill(FIELD_PHONE, self.contact.tel)
        return self
