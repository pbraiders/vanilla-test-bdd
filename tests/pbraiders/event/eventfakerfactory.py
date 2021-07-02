# coding=utf-8
"""Factory used to create an event using Faker."""

from __future__ import annotations
from dataclasses import dataclass
from faker import Faker
from pbraiders.event import Date
from pbraiders.event import Headcount
from pbraiders.event import Event
from pbraiders.event import EventAbstractFactory


@dataclass
class EventFakerFactory(EventAbstractFactory):
    """Factory used to create a event using Faker."""

    _faker: Faker

    def create(self, config: dict) -> Event:
        return Event(date=Date(),
                     age=str(self._faker.pyint(min_value=1, max_value=3, step=1)),
                     arrh=str(self._faker.pyint(min_value=1, max_value=3, step=1)),
                     comment=self._faker.text(),
                     headcount=Headcount(real=str(self._faker.pyint(min_value=0, max_value=99, step=1)),
                                         planned=str(self._faker.pyint(min_value=0, max_value=99, step=1)),
                                         canceled=str(self._faker.pyint(min_value=0, max_value=99, step=1)),
                                         max=str(self._faker.pyint(min_value=0, max_value=99, step=1))))
