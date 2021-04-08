# coding=utf-8
"""Login page."""

from dataclasses import dataclass
from pbraiders.login.User import User
from splinter import Browser
from urllib.parse import urljoin


@dataclass
class PageLogin:
    browser: Browser
    config: dict
    user: User

    # locators
    _USERNAME_FIELD = 'loginusr'
    _PASSWORD_FIELD = 'loginpwd'
    _LOGIN_BUTTON = 'login'
    _SUCCESS_MESSAGE = 'Connecté en tant que {}'

    def goTo(self):
        self.browser.visit(urljoin(str(self.config['home']), str(self.config['login'])))

    def fillName(self):
        self.browser.find_by_id(self._USERNAME_FIELD).first.fill(str(self.user.login))

    def fillPassword(self):
        self.browser.find_by_id(self._PASSWORD_FIELD).first.fill(str(self.user.password))

    def fillCredentials(self):
        self.fillName()
        self.fillPassword()

    def click(self):
        self.browser.find_by_name(self._LOGIN_BUTTON).first.click()

    def connectSuccess(self):
        self.goTo()
        self.fillName()
        self.fillPassword()
        self.click()
        assert self.browser.is_text_present(self._SUCCESS_MESSAGE.format(self.user.login)) == 1
