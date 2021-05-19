# coding=utf-8
"""New contact page."""

from __future__ import annotations
from typing import Optional
from urllib.parse import urljoin
from dataclasses import dataclass
from splinter import Browser
from pbraiders.user import User

TITLE = 'PBRaiders - Nouveau contact'
FIELD_LASTNAME = 'ctl'
FIELD_FIRSTNAME = 'ctf'
FIELD_PHONE = 'ctp'
FIELD_EMAIL = 'cte'
FIELD_ADDRESS = 'cta'
FIELD_ADDRESS_MORE = 'ctm'
FIELD_CITY = 'ctc'
FIELD_ZIP = 'ctz'

BUTTON_SEND = 'new'
FAILURE_MESSAGE = "Le nom d\'utilisateur ou les mots de passe que vous avez saisis sont incorrects."
SUCCESS_MESSAGE = "Enregistrement réussi."
USER_LIST_LOCATOR = "//*[contains(text(),'{} • ')]/.."


@dataclass
class PageAccount(object):
    """New contact page html elements and actions"""
    browser: Browser
    config: dict
    user: Optional[User] = None

    def set_user(self, user: User = None) -> PageAccount:
        """User setter"""
        self.user = user
        return self

    def on_page(self) -> bool:
        """Test if we already are on the page"""
        if self.user is None:
            return False
        return self.browser.title.lower() == TITLE.lower() and self.browser.find_by_tag('h1').first.text.lower() == self.user.login.lower()

    def visit(self) -> bool:
        """Goes to the account page"""
        # Go to users page
        self.browser.visit(urljoin(str(self.config['home']), str(self.config['users'])))
        assert self.browser.title.lower() == TITLE.lower()
        # Go to the named account
        if self.user is None:
            raise TypeError("User is not set!")
        self.browser.find_by_xpath(USER_LIST_LOCATOR.format(self.user.login)).first.click()
        return self.on_page()

    def fill_password(self) -> PageAccount:
        """Fills the password field"""
        if self.user is None:
            raise TypeError("User is not set!")
        self.browser.fill(FIELD_PASSWD, self.user.password)
        return self

    def confirm_password(self) -> PageAccount:
        """Fills the second password field"""
        if self.user is None:
            raise TypeError("User is not set!")
        self.browser.fill(FIELD_CONF_PASSWD, self.user.passwordc)
        return self

    def click(self) -> PageAccount:
        """Clicks the button"""
        self.browser.find_by_name(BUTTON_SEND).first.click()
        return self

    def check(self) -> PageAccount:
        """Activate the account"""
        self.browser.check(CHECKBOX_ACTIVATE)
        return self

    def checked(self) -> bool:
        """Return true if the the checkbox is checked"""
        return self.browser.find_by_name(CHECKBOX_ACTIVATE).first.checked

    def uncheck(self) -> PageAccount:
        """Deactivate the account"""
        self.browser.uncheck(CHECKBOX_ACTIVATE)
        return self

    def has_failed(self) -> bool:
        """Test if the password update has failed"""
        return self.browser.is_text_present(FAILURE_MESSAGE, wait_time=1)

    def has_succeeded(self) -> bool:
        """Test if the password update has succeded"""
        return self.browser.is_text_present(SUCCESS_MESSAGE, wait_time=1)
