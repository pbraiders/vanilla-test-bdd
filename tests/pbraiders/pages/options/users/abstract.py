# coding=utf-8
"""Users page extended abstraction."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from pbraiders.pages import PageAbstract
from pbraiders.user import User


@dataclass
class UserPageAbstract(PageAbstract):
    """Users page extended abstraction."""
    _user: Optional[User] = None

    @property
    def user(self) -> User | None:
        """User getter."""
        return self._user

    def set_user(self, contact: User = None) -> UserPageAbstract:
        """User setter."""
        self._user = contact
        return self
