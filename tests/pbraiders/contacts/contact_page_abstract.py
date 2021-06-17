# coding=utf-8
"""Abstract contact page."""

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
from splinter.driver import DriverAPI
from pbraiders.contact import Contact


@dataclass
class ContactPageAbstract(ABC):
    """Abstract contact page."""
    browser: DriverAPI
    config: dict
    contact: Optional[Contact] = None

    @abstractmethod
    def on_page(self) -> bool:
        pass

    @abstractmethod
    def visit(self) -> bool:
        pass

    def set_contact(self, contact: Contact = None) -> ContactPageAbstract:
        """Contact setter"""
        self.contact = contact
        return self
