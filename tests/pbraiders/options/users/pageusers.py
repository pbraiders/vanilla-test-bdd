# coding=utf-8
"""Users page."""

from __future__ import annotations
from urllib.parse import urljoin
from dataclasses import dataclass
from splinter import Browser
from pbraiders.user import User

TITLE = 'PBRaiders - Utilisateurs'
FIELD_NAME = 'usr'
FIELD_PASSWD = 'pwd'
FIELD_CONF_PASSWD = 'pwdc'
BUTTON_SEND = 'new'
FAILURE_MESSAGE = "Le nom d\'utilisateur ou les mots de passe que vous avez saisis sont incorrects."
SUCCESS_MESSAGE = "Enregistrement réussi."
USER_LIST = ' • JAMAIS • Actif'


@dataclass
class PageUsers(object):
    """Signin page html elements and actions"""
    browser: Browser
    config: dict
    user: User = None

    def set_user(self, user: User = None) -> PageUsers:
        """User setter"""
        self.user = user
        return self

    def visit(self, stay_on_the_page: bool = False) -> PageUsers:
        """Goes to the page"""
        if self.browser.title == TITLE and stay_on_the_page is True:
            return self
        self.browser.visit(urljoin(str(self.config['home']), str(self.config['users'])))
        assert self.browser.title == TITLE
        return self

    def fill_name(self) -> PageUsers:
        """Fills the name field"""
        self.browser.fill(FIELD_NAME, self.user.login)
        return self

    def fill_password(self) -> PageUsers:
        """Fills the password field"""
        self.browser.fill(FIELD_PASSWD, self.user.password)
        return self

    def confirm_password(self) -> PageUsers:
        """Fills the second password field"""
        self.browser.fill(FIELD_CONF_PASSWD, self.user.passwordc)
        return self

    def click(self) -> PageUsers:
        """Clicks the button"""
        self.browser.find_by_name(BUTTON_SEND).first.click()
        return self

    def has_failed(self) -> bool:
        """Test if the new user creation has failed"""
        return self.browser.is_text_present(FAILURE_MESSAGE) is True and self.browser.is_text_present(
            self.user.login) is False

    def has_succeeded(self) -> bool:
        """Test if the new user creation has successded"""
        return self.browser.is_text_present(SUCCESS_MESSAGE) is True and self.browser.is_text_present(
            self.user.login + USER_LIST) is True
