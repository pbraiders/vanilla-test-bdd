# coding=utf-8
"""Abstract Factory used to create user."""

from abc import ABC, abstractmethod
from pbraiders.contact import Contact


class ContactAbstractFactory(ABC):

    @abstractmethod
    def create(self, config: dict) -> Contact:
        pass

    def initialize(self, config: dict) -> Contact:
        pContact = self.create(config)
        # ... other commands if needed
        return pContact
