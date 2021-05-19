# coding=utf-8
"""Factory used to create deactivated user."""

from pbraiders.user import User
from pbraiders.user import UserAbstractFactory


class DisabledUserFactory(UserAbstractFactory):

    def create(self, config: dict) -> User:
        return User(login=config['disabled']['login'],
                    password=config['disabled']['password'],
                    passwordc=config['admin']['password'])
