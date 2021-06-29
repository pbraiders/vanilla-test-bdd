# coding=utf-8
"""Factory used to create simple user from config."""

from pbraiders.user import User
from pbraiders.user import UserAbstractFactory


class UserSimpleFactory(UserAbstractFactory):
    """Factory used to create simple user from config."""

    def create(self, config: dict) -> User:
        return User(login=config['simple']['login'],
                    password=config['simple']['password'],
                    passwordc=config['simple']['password'])
