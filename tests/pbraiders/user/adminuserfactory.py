# coding=utf-8
"""Factory used to create admin user."""

from pbraiders.user import User
from pbraiders.user import UserFactory


class AdminUserFactory(UserFactory):

    def create(self, config: dict) -> User:
        return User(login=config['admin']['login'],
                    password=config['admin']['password'])
