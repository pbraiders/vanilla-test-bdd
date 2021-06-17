# coding=utf-8
"""Contacts list page - main responsabilities."""

from urllib.parse import urljoin
from pbraiders.contacts import ContactPageAbstract

TITLE = 'PBRaiders - Contacts'
HEADER = 'Contacts'
CONTACTS_LIST = '{lastname} {firstname} • {phone}'
CONTACT_LIST_LOCATOR = "//*[contains(text(),'{lastname} {firstname} • {phone}')]/.."


class ContactsPage(ContactPageAbstract):
    """Contacts list page - main responsabilities."""

    def on_page(self) -> bool:
        """Test if we already are on the page."""
        return (TITLE.lower() in self.browser.title.lower()) and self.browser.find_by_tag('h1').first.text.lower() == HEADER.lower()

    def visit(self) -> bool:
        """Goes to the page."""
        self.browser.visit(urljoin(str(self.config['home']), str(self.config['contacts'])))
        return self.on_page()

    def visit_contact(self) -> None:
        """Goes to the page."""
        if self.contact is None:
            raise TypeError("User is not set!")
        self.browser.find_by_xpath(CONTACT_LIST_LOCATOR.format(lastname=self.contact.lastname,
                                   firstname=self.contact.firstname, phone=self.contact.tel)).first.click()

    def is_on_list(self) -> bool:
        """Test if the contact is on the list."""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        return self.browser.is_text_present(
            CONTACTS_LIST.format(lastname=self.contact.lastname, firstname=self.contact.firstname, phone=self.contact.tel),
            wait_time=1) is True
