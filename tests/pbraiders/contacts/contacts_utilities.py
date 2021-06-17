# coding=utf-8
"""Contact utilities."""


from splinter.driver import DriverAPI
from pbraiders.contact import Contact
from pbraiders.contact import ContactAbstractFactory
from pbraiders.contacts import ContactNewPage
from pbraiders.contacts import ActionContactCreate
from pbraiders.contacts import ActionContactFill
from pbraiders.signin import PageSignin
from pbraiders.signin import sign_in
from pbraiders.user import UserAbstractFactory


def new_contact(p_driver: DriverAPI, a_config: dict, p_contact_factory: ContactAbstractFactory, p_user_factory: UserAbstractFactory) -> Contact:
    """Creates a contact."""

    # Visit new contact page
    p_page = ContactNewPage(browser=p_driver, config=a_config['urls'])
    if p_page.visit() is False:
        # Sign in
        p_page_signin = PageSignin(browser=p_driver, config=a_config['urls'], user=None)
        sign_in(p_page_signin, p_user_factory.initialize(a_config["data"]["users"]))
        del p_page_signin
        # Visit new contact page
        assert p_page.visit() is True

    # Create a contact
    p_contact = p_contact_factory.initialize(config={})
    p_page.set_contact(p_contact)

    # Fill the fields
    p_fill = ActionContactFill(parent=p_page)
    p_fill.fill_lastname() \
        .fill_firstname() \
        .fill_phone() \
        .fill_zip() \
        .fill_city() \
        .fill_address_more() \
        .fill_address() \
        .fill_email()
    del p_fill

    # Create
    p_create = ActionContactCreate(parent=p_page)
    p_create.click()

    # Check
    assert p_create.has_succeeded() is True

    return p_contact
