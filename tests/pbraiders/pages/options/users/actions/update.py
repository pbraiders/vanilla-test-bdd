# coding=utf-8
"""User page - update responsability."""

from __future__ import annotations
from pbraiders.pages.options.users.actions import UserActionAbstract

BUTTON_SEND = 'new'
CHECKBOX_ACTIVATE = 'sta'
FAILURE_MESSAGE = "Le nom d\'utilisateur ou les mots de passe que vous avez saisis sont incorrects."
SUCCESS_MESSAGE = "Enregistrement réussi."


class UpdateUserAction(UserActionAbstract):
    """User page - update responsability."""

    def check(self) -> UpdateUserAction:
        """Activate the account"""
        self.page.check(CHECKBOX_ACTIVATE)
        return self

    def uncheck(self) -> UpdateUserAction:
        """Deactivate the account"""
        self.page.uncheck(CHECKBOX_ACTIVATE)
        return self

    def update(self) -> None:
        """Clicks the update button"""
        self.page.find_by_name(BUTTON_SEND).first.click()

    def has_failed(self) -> bool:
        """Test if the password update has failed"""
        return self.page.is_text_present(FAILURE_MESSAGE, wait_time=1)

    def has_succeeded(self) -> bool:
        """Test if the password update has succeded"""
        return self.page.is_text_present(SUCCESS_MESSAGE, wait_time=1)
