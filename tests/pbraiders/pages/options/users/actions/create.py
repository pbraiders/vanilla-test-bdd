# coding=utf-8
"""User page - creation responsability."""

from __future__ import annotations
from pbraiders.pages.options.users.actions import UserActionAbstract

BUTTON_SEND = 'new'
FAILURE_MESSAGE = "Le nom d\'utilisateur ou les mots de passe que vous avez saisis sont incorrects."
EXIST_MESSAGE = 'Cet utilisateur existe déjà.'
SUCCESS_MESSAGE = "Enregistrement réussi."


class CreateUserAction(UserActionAbstract):
    """User page - creation responsability."""

    def click(self) -> None:
        """Clicks the button"""
        self.page.find_by_name(BUTTON_SEND).first.click()

    def has_failed(self) -> bool:
        """Test if the new user creation has failed"""
        return self.page.is_text_present(FAILURE_MESSAGE, wait_time=1)

    def has_failed_exist(self) -> bool:
        """Test if the new user creation has failed because he's already exist"""
        return self.page.is_text_present(EXIST_MESSAGE, wait_time=1)

    def has_succeeded(self) -> bool:
        """Test if the new user creation has succeded"""
        return self.page.is_text_present(SUCCESS_MESSAGE, wait_time=1)
