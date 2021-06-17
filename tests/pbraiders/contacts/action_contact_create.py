# coding=utf-8
"""Page New Contact - create responsability."""

from pbraiders.contacts import ActionContactAbstract

BUTTON_SEND = 'new'
FAILURE_MESSAGE = "Le nom,le prénom et le numéro de téléphone doivent être renseignés."
SUCCESS_MESSAGE = "Enregistrement réussi."


class ActionContactCreate(ActionContactAbstract):
    """Page New Contact - create responsability."""

    def click(self) -> None:
        """Clicks the button"""
        self.browser.find_by_name(BUTTON_SEND).first.click()

    def has_failed(self) -> bool:
        """Test if the process has failed"""
        return self.browser.is_text_present(FAILURE_MESSAGE, wait_time=1)

    def has_succeeded(self) -> bool:
        """Test if the process has succeded"""
        return self.browser.is_text_present(SUCCESS_MESSAGE, wait_time=1)
