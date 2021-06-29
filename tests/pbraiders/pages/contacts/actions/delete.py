# coding=utf-8
"""Page Contact - delete responsability."""

from __future__ import annotations
from dataclasses import dataclass
from pbraiders.contacts import PageContact

TITLE = 'PBRaiders - Supprimer {lastname} {firstname}'
HEADER = '{lastname} {firstname}'
BUTTON_DELETE = 'del'
BUTTON_CONFIRM = 'con'
BUTTON_CANCEL = 'can'
ACTION_MESSAGE = 'Ce contact et toutes ses réservations vont être supprimés.'
SUCCESS_MESSAGE = "Suppression réussie."


@dataclass
class PageContactDelete(object):
    """Page Contact - delete responsability."""
    parent: PageContact

    def delete(self) -> PageContactDelete:
        """Clicks the delete button"""
        self.parent.browser.find_by_name(BUTTON_DELETE).first.click()
        s_title = TITLE.format(lastname=self.parent.contact.lastname, firstname=self.parent.contact.firstname)
        s_header = HEADER.format(lastname=self.parent.contact.lastname, firstname=self.parent.contact.firstname)
        assert self.parent.browser.title.lower() == s_title.lower()
        assert self.parent.browser.find_by_tag('h1').first.text.lower() == s_header.lower()
        assert self.parent.browser.is_text_present(ACTION_MESSAGE, wait_time=1) is True
        return self

    def confirm(self) -> PageContactDelete:
        """Clicks the confirm button"""
        s_title = TITLE.format(lastname=self.parent.contact.lastname, firstname=self.parent.contact.firstname)
        s_header = HEADER.format(lastname=self.parent.contact.lastname, firstname=self.parent.contact.firstname)
        assert self.parent.browser.title.lower() == s_title.lower()
        assert self.parent.browser.find_by_tag('h1').first.text.lower() == s_header.lower()
        assert self.parent.browser.is_text_present(ACTION_MESSAGE, wait_time=1) is True
        self.parent.browser.find_by_name(BUTTON_CONFIRM).first.click()
        return self

    def has_succeeded(self) -> bool:
        """Test if the process has succeded"""
        return self.parent.browser.is_text_present(SUCCESS_MESSAGE, wait_time=1)
