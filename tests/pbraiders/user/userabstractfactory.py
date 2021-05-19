# coding=utf-8
"""Abstract Factory used to create user."""

from abc import ABC, abstractmethod
from pbraiders.user import User


class UserAbstractFactory(ABC):

    @abstractmethod
    def create(self, config: dict) -> User:
        pass

    def initialize(self, config: dict) -> User:
        pUser = self.create(config)
        # ... other commands if needed
        return pUser
