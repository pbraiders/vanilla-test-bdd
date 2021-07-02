# coding=utf-8
"""Event page - delete responsability."""

from __future__ import annotations
from pbraiders.pages.events.actions import BUTTON_CANCEL
from pbraiders.pages.events.actions import BUTTON_CONFIRM
from pbraiders.pages.events.actions import BUTTON_DELETE
from pbraiders.pages.events.actions import EventActionAbstract

TITLE = 'PBRaiders - Supprimer une réservation'
HEADER = '{date} - {lastname} {firstname}'
MESSAGE_ACTION = 'Cette réservation va être supprimée.'
MESSAGE_SUCCESS = "Suppression réussie."


class EventDeleteAction(EventActionAbstract):
    """Event page - delete responsability."""

    def delete(self) -> EventDeleteAction:
        """Clicks the delete button."""
        self.page.find_by_name(BUTTON_DELETE).first.click()
        return self

    def confirm(self) -> None:
        """Clicks the confirm button."""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        if self.event is None:
            raise TypeError("Event is not set!")
        s_date_name = self.event.date.date_name()
        s_header = HEADER.format(date=s_date_name, lastname=self.contact.lastname, firstname=self.contact.firstname)
        assert self.page.title.lower() == TITLE.lower()
        assert self.page.find_by_tag('h1').first.text.lower() == s_header.lower()
        assert self.page.is_text_present(MESSAGE_ACTION, wait_time=1) is True
        self.page.find_by_name(BUTTON_CONFIRM).first.click()

    def cancel(self) -> None:
        """Clicks the cancel button."""
        self.page.find_by_name(BUTTON_CANCEL).first.click()

    def has_succeeded(self) -> bool:
        """Test if the process has succeded"""
        return self.page.is_text_present(MESSAGE_SUCCESS, wait_time=1)
