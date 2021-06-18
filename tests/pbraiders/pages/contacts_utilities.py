# coding=utf-8
"""Contact utilities."""


from splinter.driver import DriverAPI
from pbraiders.contact import Contact
from pbraiders.user import User
from pbraiders.pages.contacts import ContactNewPage
from pbraiders.pages.contacts.actions import CreateContactAction
from pbraiders.pages.contacts.actions import FillContactAction
from pbraiders.pages import sign_in


def new_contact(driver: DriverAPI, config: dict, contact: Contact, user: User) -> bool:
    """Creates a contact."""

    # Visit new contact page
    p_page = ContactNewPage(_driver=driver, _config=config['urls'])
    if p_page.visit() is False:
        assert sign_in(driver=driver, config=config['urls'], user=user) is True
        assert p_page.visit() is True

    # Fill the fields
    p_page.set_contact(contact)
    p_action = FillContactAction(_page=p_page)
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
    p_action = CreateContactAction(_page=p_page)
    p_action.click()

    # Check
    return p_action.has_succeeded()
