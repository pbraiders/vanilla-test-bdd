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
from pbraiders.pages.contacts.actions import CreateContactAction  # pylint: disable=import-error
from pbraiders.pages.contacts.actions import FillContactAction  # pylint: disable=import-error
from pbraiders.pages.contacts import ContactNewPage  # pylint: disable=import-error
from pbraiders.pages.contacts import ContactPage  # pylint: disable=import-error
from pbraiders.pages.contacts import ContactsPage  # pylint: disable=import-error
from pbraiders.pages.signin_utilities import sign_in  # pylint: disable=import-error

scenario = partial(scenario, 'contacts/contact_create_success.feature')


@scenario('Create the contact')
def test_create_new_contact() -> None:
    """Create the contact."""


@given('I am on the new contact page', target_fixture="page_contact_new")
def page_contact_new(the_config, the_browser, the_database) -> ContactNewPage:
    """I am on the new contact page."""
    p_page = ContactNewPage(_driver=the_browser, _config=the_config['urls'])
    if p_page.visit() is False:
        # Sign in
        assert sign_in(driver=the_browser, config=the_config, user="simple") is True
        # Visit users page
        assert p_page.visit() is True
    return p_page


@given('I have a new contact to create', target_fixture="contact_new")
def contact_new(the_faker) -> Contact:
    """I have a new contact to create."""
    return ContactFakerFactory(_faker=the_faker).create(config={})


@when('I create the contact')
def contact_create(page_contact_new, contact_new) -> None:
    """I create the contact."""
    page_contact_new.set_contact(contact_new)
    p_action = FillContactAction(_page=page_contact_new)
    p_action.fill_lastname() \
        .fill_firstname() \
        .fill_phone() \
        .fill_zip() \
        .fill_city() \
        .fill_address_more() \
        .fill_address() \
        .fill_email()
    del p_action
    p_action = CreateContactAction(_page=page_contact_new)
    p_action.click()


@then('I should see the success message')
def success_message(page_contact_new) -> None:
    """I should see the success message."""
    p_action = CreateContactAction(_page=page_contact_new)
    assert p_action.has_succeeded() is True


@then('It should appear on the contact list')
def contact_list(the_config, the_browser, contact_new):
    """It should appear on the contact list."""
    p_page = ContactsPage(_driver=the_browser, _config=the_config['urls'], _contact=contact_new)
    if p_page.on_page() is False:
        assert p_page.visit() is True
    assert p_page.is_on_list() is True


@then('I should access to this contact page')
def conctact_page(the_config, the_browser, contact_new):
    """I should access to this contact page."""
    p_page = ContactPage(_driver=the_browser, _config=the_config['urls'], _contact=contact_new)
    assert p_page.visit() is True
    assert p_page.is_contact_present() is True
