# coding=utf-8
"""Sign-in page - sign-in responsability."""

from __future__ import annotations
from pbraiders.pages.signin.actions import SigninActionAbstract

USERNAME_FIELD = "loginusr"
PASSWORD_FIELD = "loginpwd"
LOGIN_BUTTON = "login"
FAILURE_MESSAGE = "Le nom d\'utilisateur ou le mot de passe que vous avez saisi est incorrect."
CONNECTED_MESSAGE = "Connecté en tant que {}"


class SigninAction(SigninActionAbstract):
    """Sign-in page - sign-in responsability."""

    def fill_name(self) -> SigninAction:
        """Fills the name field"""
        self.page.find_by_id(USERNAME_FIELD).first.fill(str(self.user.login))
        return self

    def fill_password(self) -> SigninAction:
        """Fills the password field"""
        self.page.find_by_id(PASSWORD_FIELD).first.fill(str(self.user.password))
        return self

    def fill_credential(self) -> SigninAction:
        """Fills the credential fields"""
        self.fill_name()
        self.fill_password()
        return self

    def click(self) -> SigninAction:
        """Clicks the button"""
        self.page.find_by_name(LOGIN_BUTTON).first.click()
        return self

    def connected(self) -> bool:
        """Tests if user is connected"""
        if self.user is None:
            raise TypeError("User is not set!")

        return self.page.is_text_present(
            CONNECTED_MESSAGE.format(self.user.login),
            wait_time=1)

    def has_failed(self) -> bool:
        """Test if an error is displayed"""
        return self.page.is_text_present(FAILURE_MESSAGE, wait_time=1)
