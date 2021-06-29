# coding=utf-8
"""Users list page - main responsabilities."""

from urllib.parse import urljoin
from pbraiders.pages.options.users import UserPageAbstract

TITLE = 'PBRaiders - Utilisateurs'
HEADER = 'Utilisateurs'
USER_LIST = '{name} • '
USER_LIST_LOCATOR = "//*[contains(text(),'{name} • ')]/.."


class UsersPage(UserPageAbstract):
    """Users list page - main responsabilities."""

    def on_page(self) -> bool:
        """Returns True if we are visiting this page."""
        return self.page.title.lower() == TITLE.lower() and self.page.find_by_tag('h1').first.text.lower() == HEADER.lower()

    def visit(self) -> bool:
        """Goes to the page"""
        self.page.visit(urljoin(str(self.config['home']), str(self.config['users'])))
        return self.on_page()

    def visit_user(self) -> None:
        """Goes to the user account page."""
        if self.user is None:
            raise TypeError("User is not set!")
        self.page.find_by_xpath(USER_LIST_LOCATOR.format(name=self.user.login)).first.click()

    def is_on_list(self) -> bool:
        """Return true if the user is on the list."""
        if self.user is None:
            raise TypeError("User is not set!")
        return self.page.is_text_present(USER_LIST.format(name=self.user.login), wait_time=1) is True
