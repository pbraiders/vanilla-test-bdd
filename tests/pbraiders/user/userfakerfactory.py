# coding=utf-8
"""Factory used to create simple user using Faker."""

from __future__ import annotations
from dataclasses import dataclass
from faker import Faker
from pbraiders.user import User
from pbraiders.user import UserAbstractFactory


@dataclass
class UserFakerFactory(UserAbstractFactory):
    """Factory used to create simple user using Faker."""

    _faker: Faker

    def create(self, config: dict) -> User:
        s_name = self._faker.first_name()
        s_passwd = s_name + 'password'
        return User(login=s_name, password=s_passwd, passwordc=s_passwd)
