# coding=utf-8
"""Event page - creation responsability."""

from __future__ import annotations
from pbraiders.pages.events.actions import EventActionAbstract

BUTTON_SEND = 'new'
FAILURE_MESSAGE = "Le nom,le prénom et le numéro de téléphone doivent être renseignés."
SUCCESS_MESSAGE = "Enregistrement réussi."


class EventCreateAction(EventActionAbstract):
    """Event page - creation responsability."""

    def click(self) -> None:
        """Clicks the button"""
        self.page.find_by_name(BUTTON_SEND).first.click()

    def has_failed(self) -> bool:
        """Test if the process has failed"""
        return self.page.is_text_present(FAILURE_MESSAGE, wait_time=1)

    def has_succeeded(self) -> bool:
        """Test if the process has succeded"""
        return self.page.is_text_present(SUCCESS_MESSAGE, wait_time=1)
