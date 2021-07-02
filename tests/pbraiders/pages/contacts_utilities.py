# coding=utf-8
"""Contact utilities."""


from splinter.driver import DriverAPI
from pbraiders.contact import Contact
from pbraiders.pages.contacts import ContactNewPage
from pbraiders.pages.contacts import ContactPage
from pbraiders.pages.contacts.actions import ContactCreateAction
from pbraiders.pages.contacts.actions import ContactReadAction
from pbraiders.pages.contacts.actions import ContactWriteAction


def new_contact(driver: DriverAPI, config: dict, contact: Contact) -> bool:
    """Creates a contact.
       config=config['urls']"""

    # Visit new contact page
    p_page = ContactNewPage(_driver=driver, _config=config, _contact=contact)
    assert p_page.visit() is True

    # Fill the fields
    p_action = ContactWriteAction(_page=p_page)
    p_action.fill_lastname() \
            .fill_firstname() \
            .fill_phone() \
            .fill_zip() \
            .fill_city() \
            .fill_address_more() \
            .fill_address() \
            .fill_email()
    del p_action

    # Create
    p_action = ContactCreateAction(_page=p_page)
    p_action.click()

    # Check
    return p_action.has_succeeded()


def verify_contact(page: ContactPage) -> bool:
    """Verifies if the fields are filled as expected."""
    p_action = ContactReadAction(_page=page)
    return p_action.is_equal_lastname() is True and \
        p_action.is_equal_firstname() is True and\
        p_action.is_equal_phone() is True and\
        p_action.is_equal_zip() is True and\
        p_action.is_equal_city() is True and \
        p_action.is_equal_address_more() is True and \
        p_action.is_equal_address() is True and \
        p_action.is_equal_email() is True


def verify_contact_with_comment(page: ContactPage) -> bool:
    """Verifies if the fields are filled as expected."""
    p_action = ContactReadAction(_page=page)
    return verify_contact(page) is True and p_action.is_equal_comment() is True
