# coding=utf-8
"""Factory used to create a contact using Faker."""

from __future__ import annotations
from dataclasses import dataclass
from faker import Faker
from pbraiders.contact import Contact
from pbraiders.contact import ContactAbstractFactory


@dataclass
class ContactFakerFactory(ContactAbstractFactory):
    """Factory used to create a contact using Faker."""

    _faker: Faker

    def create(self, config: dict) -> Contact:
        return Contact(
            lastname=self._faker.last_name(),
            firstname=self._faker.first_name(),
            tel=self._faker.phone_number(),
            email=self._faker.email(),
            address=self._faker.street_address(),
            address_more=self._faker.country(),
            city=self._faker.city(),
            zip=self._faker.postcode(),
            comment=self._faker.text())
