# coding=utf-8
"""User page - main responsabilities."""

from urllib.parse import urljoin
from pbraiders.pages.options.users import UserPageAbstract

TITLE = 'PBRaiders - Utilisateurs'
CHECKBOX_ACTIVATE = 'sta'
USER_LIST_LOCATOR = "//*[contains(text(),'{name} • ')]/.."


class UserPage(UserPageAbstract):
    """User page - main responsabilities."""

    def on_page(self) -> bool:
        """Returns True if we are visiting this page."""
        if self.user is None:
            raise TypeError("User is not set!")
        return self.page.title.lower() == TITLE.lower() and self.page.find_by_tag('h1').first.text.lower() == self.user.login.lower()

    def visit(self) -> bool:
        """Goes to the page."""
        if self.user is None:
            raise TypeError("User is not set!")

        try:
            self.page.visit(urljoin(str(self.config['home']), str(self.config['users'])))
            self.page.find_by_xpath(USER_LIST_LOCATOR.format(name=self.user.login)).first.click()
        except Exception:
            return False

        return self.on_page()

    def checked(self) -> bool:
        """Return true if the the checkbox is checked"""
        return self.page.find_by_name(CHECKBOX_ACTIVATE).first.checked
