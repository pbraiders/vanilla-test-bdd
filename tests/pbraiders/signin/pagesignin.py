# coding=utf-8
"""Sign in page."""

from __future__ import annotations
from urllib.parse import urljoin
from dataclasses import dataclass
from pbraiders.user import User
from splinter import Browser

TITLE = "PBRaiders - Connexion"
USERNAME_FIELD = "loginusr"
PASSWORD_FIELD = "loginpwd"
LOGIN_BUTTON = "login"
SUCCESS_MESSAGE = "Connecté en tant que {}"
FAILURE_MESSAGE = "Le nom d\'utilisateur ou le mot de passe que vous avez saisi est incorrect."


@dataclass
class PageSignin(object):
    """Signin page html elements and actions"""
    browser: Browser
    config: dict
    user: User

    def visit(self, stay_on_the_page: bool = False) -> PageSignin:
        """Goes to the page"""
        if self.browser.title == TITLE and stay_on_the_page is True:
            return self
        self.browser.visit(urljoin(str(self.config['home']), str(self.config['signin'])))
        assert self.browser.title == TITLE
        return self

    def sign_out(self) -> PageSignin:
        """Goes to the sign out page"""
        self.browser.visit(urljoin(str(self.config['home']), str(self.config['signout'])))
        return self

    def fill_name(self) -> PageSignin:
        """Fills the name field"""
        self.browser.find_by_id(USERNAME_FIELD).first.fill(str(self.user.login))
        return self

    def fill_password(self) -> PageSignin:
        """Fills the password field"""
        self.browser.find_by_id(PASSWORD_FIELD).first.fill(str(self.user.password))
        return self

    def fill_credentials(self) -> PageSignin:
        """Fills the credential fields"""
        self.fill_name()
        self.fill_password()
        return self

    def click(self) -> PageSignin:
        """Clicks the button"""
        self.browser.find_by_name(LOGIN_BUTTON).first.click()
        return self

    def connect_success(self):
        """Connecting"""
        self.visit()
        self.fill_name()
        self.fill_password()
        self.click()
        assert self.connected() is True

    def connected(self) -> bool:
        """Tests if user is connected"""
        return self.browser.is_text_present(
            SUCCESS_MESSAGE.format(self.user.login),
            wait_time=2) is True

    def has_failed(self) -> bool:
        """Test if an error is displayed"""
        return self.browser.is_text_present(FAILURE_MESSAGE,
                                            wait_time=2) is True
