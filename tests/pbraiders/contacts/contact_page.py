# coding=utf-8
"""Contact page - main responsabilities."""

from urllib.parse import urljoin
from pbraiders.contacts import ContactPageAbstract

TITLE = 'PBRaiders - {lastname} {firstname}'
HEADER = '{lastname} {firstname}'
CONTACT_LIST_LOCATOR = "//*[contains(text(),'{lastname} {firstname} • {phone}')]/.."


class ContactPage(ContactPageAbstract):
    """Contact page - main responsabilities."""

    def on_page(self) -> bool:
        """Test if we already are on the page"""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        s_title = TITLE.format(lastname=self.contact.lastname, firstname=self.contact.firstname)
        s_header = HEADER.format(lastname=self.contact.lastname, firstname=self.contact.firstname)
        return (self.browser.title.lower() == s_title.lower()) and (self.browser.find_by_tag('h1').first.text.lower() == s_header.lower())

    def visit(self) -> bool:
        """Goes to the page."""
        if self.contact is None:
            raise TypeError("User is not set!")
        try:
            self.browser.visit(urljoin(str(self.config['home']), str(self.config['contacts'])))
            self.browser.find_by_xpath(CONTACT_LIST_LOCATOR.format(lastname=self.contact.lastname,
                                       firstname=self.contact.firstname, phone=self.contact.tel)).first.click()
        except Exception:
            pass
        return self.on_page()

    def is_contact_present(self) -> bool:
        """Returns true if all the contact's values can be found on the page."""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        return self.browser.is_element_present_by_value(self.contact.firstname) \
            and self.browser.is_element_present_by_value(self.contact.lastname) \
            and self.browser.is_element_present_by_value(self.contact.tel) \
            and self.browser.is_element_present_by_value(self.contact.email) \
            and self.browser.is_element_present_by_value(self.contact.address) \
            and self.browser.is_element_present_by_value(self.contact.address_more) \
            and self.browser.is_element_present_by_value(self.contact.city) \
            and self.browser.is_element_present_by_value(self.contact.zip)

    def is_contact_comments_present(self) -> bool:
        """Returns true if all the contact's comment can be found on the page."""
        return self.browser.is_element_present_by_value(self.contact.comment)
