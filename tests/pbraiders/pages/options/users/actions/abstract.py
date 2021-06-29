# coding=utf-8
"""User action abstraction."""

from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from splinter.driver import DriverAPI
from pbraiders.pages.options.users import UserPageAbstract
from pbraiders.user import User


@dataclass
class UserActionAbstract(ABC):
    """User action abstraction."""
    _page: UserPageAbstract

    @property
    def page(self) -> DriverAPI:
        """Returns driver instance."""
        return self._page.page

    @property
    def user(self) -> User:
        """Returns user instance."""
        if self._page.user is None:
            raise TypeError("User is not set!")
        return self._page.user
