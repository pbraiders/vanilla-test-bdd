from __future__ import annotations
from abc import ABC, abstractmethod
from pbraiders.login.User import User
from urllib.parse import urljoin


class UserFactory(ABC):

    @abstractmethod
    def create(self, config: dict):
        pass

    def initialize(self, theConfig) -> User:
        pUser = self.create(theConfig['users'])
        pUser.logouturl = urljoin(theConfig['urls']['home'], theConfig['urls']['logout'])
        return pUser


class AdminFactory(UserFactory):

    def create(self, config: dict) -> User:
        return User(login=config['admin']['login'],
                    password=config['admin']['password'],
                    logouturl='')


class SimpleFactory(UserFactory):

    def create(self, config: dict) -> User:
        return User(login=config['simple']['login'],
                    password=config['simple']['password'],
                    logouturl='')
