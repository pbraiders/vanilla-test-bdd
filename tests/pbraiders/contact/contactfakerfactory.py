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

    faker: Faker

    def create(self, config: dict) -> Contact:
        return Contact(
            lastname=self.faker.last_name(),
            firstname=self.faker.first_name(),
            tel=self.faker.phone_number(),
            email=self.faker.email(),
            address=self.faker.street_address(),
            address_more=self.faker.country(),
            city=self.faker.city(),
            zip=self.faker.postcode(),
            comment=self.faker.text())
