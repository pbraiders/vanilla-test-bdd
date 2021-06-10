# coding=utf-8
"""Contact creation, success cases."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.contact import Contact  # pylint: disable=import-error
from pbraiders.contact import ContactFakerFactory  # pylint: disable=import-error
from pbraiders.contacts import PageContact  # pylint: disable=import-error
from pbraiders.contacts import PageContacts  # pylint: disable=import-error
from pbraiders.contacts import PageContactNew  # pylint: disable=import-error
from pbraiders.signin import PageSignin  # pylint: disable=import-error
from pbraiders.signin import sign_in  # pylint: disable=import-error
from pbraiders.user import UserSimpleFactory  # pylint: disable=import-error

scenario = partial(scenario, 'contacts/contact_create_success.feature')


@scenario('Create the contact')
def test_create_new_contact() -> None:
    """Create the contact."""


@given('I am on the new contact page', target_fixture="page_contact_new")
def page_contact_new(the_config, the_browser, the_database) -> PageContactNew:
    """I am on the new contact page."""
    p_page_contact_new = PageContactNew(browser=the_browser, config=the_config['urls'])
    if p_page_contact_new.visit() is False:
        # Sign in
        p_page_signin = PageSignin(browser=the_browser, config=the_config['urls'], user=None)
        sign_in(p_page_signin, UserSimpleFactory().initialize(the_config["data"]["users"]))
        del p_page_signin
        # Visit new contact page
        assert p_page_contact_new.visit() is True
    return p_page_contact_new


@given('I have a new contact to create', target_fixture="contact_new")
def contact_new(the_faker) -> Contact:
    """I have a new contact to create."""
    p_Factory = ContactFakerFactory(faker=the_faker)
    p_Contact = p_Factory.create(config={})
    return p_Contact


@when('I create the contact')
def contact_create(page_contact_new, contact_new) -> None:
    """I create the contact."""
    page_contact_new.set_contact(contact_new) \
        .fill_lastname() \
        .fill_firstname() \
        .fill_phone() \
        .fill_zip() \
        .fill_city() \
        .fill_address_more() \
        .fill_address() \
        .fill_email() \
        .click()


@then('I should see the success message')
def success_message(page_contact_new) -> None:
    """I should see the success message."""
    assert page_contact_new.has_succeeded() is True


@then('It should appear on the contact list')
def contact_list(the_config, the_browser, contact_new):
    """It should appear on the contact list."""
    p_page_contacts = PageContacts(browser=the_browser, config=the_config['urls'], contact=contact_new)
    if p_page_contacts.on_page() is False:
        assert p_page_contacts.visit() is True
    assert p_page_contacts.is_on_list() is True


@then('I should access to this contact page')
def conctact_page(the_config, the_browser, contact_new):
    """I should access to this contact page."""
    p_page_contact = PageContact(browser=the_browser, config=the_config['urls'], contact=contact_new)
    assert p_page_contact.visit() is True and p_page_contact.is_contact_present() is True
