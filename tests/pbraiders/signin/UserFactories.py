# coding=utf-8
"""Factories used to create user."""

from abc import ABC, abstractmethod
from pbraiders.signin.User import User
from urllib.parse import urljoin


class UserFactory(ABC):

    @abstractmethod
    def create(self, config: dict) -> User:
        pass

    def initialize(self, config: dict) -> User:
        pUser = self.create(config['users'])
        # ... other commands if needed
        return pUser


class AdminFactory(UserFactory):

    def create(self, config: dict) -> User:
        return User(login=config['admin']['login'],
                    password=config['admin']['password'])


class SimpleFactory(UserFactory):

    def create(self, config: dict) -> User:
        return User(login=config['simple']['login'],
                    password=config['simple']['password'])
