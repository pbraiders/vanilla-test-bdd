# coding=utf-8
"""Sign-in action abstraction."""

from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from splinter.driver import DriverAPI
from pbraiders.pages.signin import SigninPageAbstract
from pbraiders.user import User


@dataclass
class SigninActionAbstract(ABC):
    """Sign-in action abstraction."""
    _page: SigninPageAbstract

    @property
    def page(self) -> DriverAPI:
        """Returns page's driver instance."""
        return self._page.page

    @property
    def user(self) -> User:
        """Returns page's user instance."""
        if self._page.user is None:
            raise TypeError("User is not set!")
        return self._page.user
