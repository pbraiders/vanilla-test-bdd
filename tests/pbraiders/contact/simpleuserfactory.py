# coding=utf-8
"""Factory used to create simple user."""

from pbraiders.user import User
from pbraiders.user import UserAbstractFactory


class SimpleUserFactory(UserAbstractFactory):

    def create(self, config: dict) -> User:
        return User(login=config['simple']['login'],
                    password=config['simple']['password'],
                    passwordc=config['admin']['password'])
