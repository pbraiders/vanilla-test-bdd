# coding=utf-8
"""Users page."""

from __future__ import annotations
from urllib.parse import urljoin
from dataclasses import dataclass
from splinter import Browser
from pbraiders.user import User

TITLE = 'PBRaiders - Utilisateurs'
HEADER = '<h1>Utilisateurs</h1>'
FIELD_NAME = 'usr'
FIELD_PASSWD = 'pwd'
FIELD_CONF_PASSWD = 'pwdc'
BUTTON_SEND = 'new'
FAILURE_MESSAGE = "Le nom d\'utilisateur ou les mots de passe que vous avez saisis sont incorrects."
EXIST_MESSAGE = 'Cet utilisateur existe déjà.'
SUCCESS_MESSAGE = "Enregistrement réussi."
USER_LIST_ACTIF = ' • JAMAIS • Actif'
USER_LIST_NAME = ' • '


@dataclass
class PageUsers(object):
    """Users page html elements and actions"""
    browser: Browser
    config: dict
    user: User = None

    def set_user(self, user: User = None) -> PageUsers:
        """User setter"""
        self.user = user
        return self

    def on_page(self) -> bool:
        """Test if we already are on the page"""
        return self.browser.title.lower() == TITLE.lower() and self.browser.is_text_present(HEADER, wait_time=1)

    def visit(self) -> PageUsers:
        """Goes to the page"""
        self.browser.visit(urljoin(str(self.config['home']), str(self.config['users'])))
        assert self.browser.title == TITLE
        return self

    def fill_name(self) -> PageUsers:
        """Fills the name field"""
        if self.user is None:
            raise TypeError("User is not set!")
        self.browser.fill(FIELD_NAME, self.user.login)
        return self

    def fill_password(self) -> PageUsers:
        """Fills the password field"""
        if self.user is None:
            raise TypeError("User is not set!")
        self.browser.fill(FIELD_PASSWD, self.user.password)
        return self

    def confirm_password(self) -> PageUsers:
        """Fills the second password field"""
        if self.user is None:
            raise TypeError("User is not set!")
        self.browser.fill(FIELD_CONF_PASSWD, self.user.passwordc)
        return self

    def click(self) -> PageUsers:
        """Clicks the button"""
        self.browser.find_by_name(BUTTON_SEND).first.click()
        return self

    def has_failed(self) -> bool:
        """Test if the new user creation has failed"""
        if self.user is None:
            raise TypeError("User is not set!")
        return self.browser.is_text_present(
            FAILURE_MESSAGE, wait_time=1) and self.browser.is_text_present(
            self.user.login + USER_LIST_NAME, wait_time=1) is False

    def has_failed_exist(self) -> bool:
        """Test if the new user creation has failed because he's already exist"""
        if self.user is None:
            raise TypeError("User is not set!")
        return self.browser.is_text_present(
            EXIST_MESSAGE, wait_time=1) and self.browser.is_text_present(
            self.user.login + USER_LIST_NAME, wait_time=1)

    def has_succeeded(self) -> bool:
        """Test if the new user creation has successded"""
        if self.user is None:
            raise TypeError("User is not set!")
        return self.browser.is_text_present(
            SUCCESS_MESSAGE, wait_time=1) and self.browser.is_text_present(
            self.user.login + USER_LIST_ACTIF, wait_time=1)
