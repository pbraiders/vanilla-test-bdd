# coding=utf-8
"""Contact page - is_equal fields responsability."""

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


class ContactReadAction(ContactActionAbstract):

    def is_equal_zip(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_ZIP)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value).lower() == str(self.contact.zip).lower()

    def is_equal_city(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_CITY)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value).lower() == str(self.contact.city).lower()

    def is_equal_address_more(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_ADDRESS_MORE)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value).lower() == str(self.contact.address_more).lower()

    def is_equal_address(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_ADDRESS)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value).lower() == str(self.contact.address).lower()

    def is_equal_comment(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_COMMENT)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value).lower() == str(self.contact.comment).lower()

    def is_equal_email(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_EMAIL)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value).lower() == str(self.contact.email).lower()

    def is_equal_lastname(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_LASTNAME)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value).lower() == str(self.contact.lastname).lower()

    def is_equal_firstname(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_FIRSTNAME)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value).lower() == str(self.contact.firstname).lower()

    def is_equal_phone(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_PHONE)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value).lower() == str(self.contact.tel).lower()
