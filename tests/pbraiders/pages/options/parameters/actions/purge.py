# coding=utf-8
"""Parameters page - purge responsability."""

from __future__ import annotations
from pbraiders.pages.options.parameters.actions import ParametersActionAbstract

FIELD_PURGE = 'rey'
BUTTON_SEND = 'Envoyer'
BUTTON_CONFIRM = 'con'
BUTTON_CANCEL = 'can'
FAILURE_MESSAGE = "La date saisie n'est pas valide."
SUCCESS_MESSAGE = "Suppression réussie."
CONFIRM_MESSAGE = 'Toutes les réservations antérieures à {0} vont être supprimées'


class PurgeAction(ParametersActionAbstract):
    """Parameters page - purge responsability."""
    _year: str

    def fill(self, value: str = None) -> PurgeAction:
        """Fills the purge field."""
        if value is not None:
            self.page.fill(FIELD_PURGE, int(value))
            self._year = value
        return self

    def purge(self) -> PurgeAction:
        """Clicks the purge button"""
        self.page.find_by_value(BUTTON_SEND).first.click()
        return self

    def on_confirm_page(self) -> bool:
        """Test if we are on the page"""
        return self.page.is_text_present(CONFIRM_MESSAGE.format(self._year))

    def cancel(self) -> PurgeAction:
        """Cancel the deletion."""
        self.page.find_by_name(BUTTON_CANCEL).first.click()
        return self

    def confirm(self) -> PurgeAction:
        """Confirm the deletion."""
        self.page.find_by_name(BUTTON_CONFIRM).first.click()
        return self

    def has_failed(self) -> bool:
        """Test if the purge has failed"""
        return self.page.is_text_present(FAILURE_MESSAGE, wait_time=1)

    def has_succeeded(self) -> bool:
        """Test if the purge has succeded"""
        return self.page.is_text_present(SUCCESS_MESSAGE, wait_time=1)
