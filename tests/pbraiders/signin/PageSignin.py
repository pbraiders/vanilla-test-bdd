# coding=utf-8
"""Sign in page."""

from dataclasses import dataclass
from pbraiders.signin.User import User
from splinter import Browser
from urllib.parse import urljoin


@dataclass
class PageSignin:
    browser: Browser
    config: dict
    user: User

    # locators
    _TITLE = 'PBRaiders - Connexion'
    _USERNAME_FIELD = 'loginusr'
    _PASSWORD_FIELD = 'loginpwd'
    _LOGIN_BUTTON = 'login'
    _SUCCESS_MESSAGE = 'Connecté en tant que {}'
    _FAILURE_MESSAGE = 'Le nom d\'utilisateur ou le mot de passe que vous avez saisi est incorrect.'

    def visit(self, stay_on_the_page: bool = False):
        if self.browser.title == self._TITLE and stay_on_the_page == True:
            return self
        self.browser.visit(urljoin(str(self.config['home']), str(self.config['signin'])))
        assert self.browser.title == self._TITLE
        return self

    def signOut(self):
        self.browser.visit(urljoin(str(self.config['home']), str(self.config['signout'])))
        return self

    def fillName(self):
        self.browser.find_by_id(self._USERNAME_FIELD).first.fill(str(self.user.login))
        return self

    def fillPassword(self):
        self.browser.find_by_id(self._PASSWORD_FIELD).first.fill(str(self.user.password))
        return self

    def fillCredentials(self):
        self.fillName()
        self.fillPassword()
        return self

    def click(self):
        self.browser.find_by_name(self._LOGIN_BUTTON).first.click()

    def connectSuccess(self):
        self.goTo()
        self.fillName()
        self.fillPassword()
        self.click()
        assert self.connected() == True

    def connected(self) -> bool:
        return self.browser.is_text_present(self._SUCCESS_MESSAGE.format(self.user.login), wait_time=2) == True

    def hasFail(self):
        assert self.browser.is_text_present(self._FAILURE_MESSAGE) == True
