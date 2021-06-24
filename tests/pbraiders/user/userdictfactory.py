# coding=utf-8
"""Factory used to create user from dict."""

from pbraiders.user import User  # pylint: disable=import-error
from pbraiders.user import UserAbstractFactory  # pylint: disable=import-error


class UserDictFactory(UserAbstractFactory):
    """Factory used to create user from dict.
        config={
                "login": "...",
                "password": "..."
            }"""

    def create(self, config: dict) -> User:
        return User(login=config['login'],
                    password=config['password'],
                    passwordc=config['password'])
