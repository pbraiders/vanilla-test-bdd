# coding=utf-8
"""User page - fill fields responsability."""

from __future__ import annotations
from pbraiders.pages.options.users.actions import UserActionAbstract

FIELD_NAME = 'usr'
FIELD_PASSWD = 'pwd'
FIELD_CONF_PASSWD = 'pwdc'
CHECKBOX_ACTIVATE = 'sta'


class FillUserAction(UserActionAbstract):
    """User page - fill fields responsability."""

    def fill_name(self) -> FillUserAction:
        """Fills the name field"""
        self.page.fill(FIELD_NAME, self.user.login)
        return self

    def fill_password(self) -> FillUserAction:
        """Fills the password field"""
        self.page.fill(FIELD_PASSWD, self.user.password)
        return self

    def confirm_password(self) -> FillUserAction:
        """Fills the second password field"""
        self.page.fill(FIELD_CONF_PASSWD, self.user.passwordc)
        return self
