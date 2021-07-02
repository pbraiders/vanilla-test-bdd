# coding=utf-8
"""Abstract Factory used to create event."""

from abc import ABC, abstractmethod
from pbraiders.event import Event


class EventAbstractFactory(ABC):

    @abstractmethod
    def create(self, config: dict) -> Event:
        pass

    def initialize(self, config: dict) -> Event:
        pEvent = self.create(config)
        # ... other commands if needed
        return pEvent
