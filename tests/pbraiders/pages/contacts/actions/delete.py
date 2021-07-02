# coding=utf-8
"""Contact page - delete responsability."""

from __future__ import annotations
from pbraiders.pages.contacts.actions import BUTTON_CANCEL
from pbraiders.pages.contacts.actions import BUTTON_CONFIRM
from pbraiders.pages.contacts.actions import BUTTON_DELETE
from pbraiders.pages.contacts.actions import ContactActionAbstract

TITLE = 'PBRaiders - Supprimer {lastname} {firstname}'
HEADER = '{lastname} {firstname}'
MESSAGE_ACTION = 'Ce contact et toutes ses réservations vont être supprimés.'
MESSAGE_SUCCESS = "Suppression réussie."


class ContactDeleteAction(ContactActionAbstract):
    """Contact page - delete responsability."""

    def delete(self) -> ContactDeleteAction:
        """Clicks the delete button."""
        self.page.find_by_name(BUTTON_DELETE).first.click()
        return self

    def confirm(self) -> None:
        """Clicks the confirm button."""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        s_title = TITLE.format(lastname=self.contact.lastname, firstname=self.contact.firstname)
        s_header = HEADER.format(lastname=self.contact.lastname, firstname=self.contact.firstname)
        assert self.page.title.lower() == s_title.lower()
        assert self.page.find_by_tag('h1').first.text.lower() == s_header.lower()
        assert self.page.is_text_present(MESSAGE_ACTION, wait_time=1) is True
        self.page.find_by_name(BUTTON_CONFIRM).first.click()

    def cancel(self) -> None:
        """Clicks the cancel button."""
        self.page.find_by_name(BUTTON_CANCEL).first.click()

    def has_succeeded(self) -> bool:
        """Test if the process has succeded"""
        return self.page.is_text_present(MESSAGE_SUCCESS, wait_time=1)
