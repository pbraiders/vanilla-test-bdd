# coding=utf-8
"""Contact creation, failure cases."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.contact import ContactFakerFactory  # pylint: disable=import-error
from pbraiders.pages.contacts.actions import ContactCreateAction  # pylint: disable=import-error
from pbraiders.pages.contacts.actions import ContactWriteAction  # pylint: disable=import-error
from pbraiders.pages.contacts import ContactNewPage  # pylint: disable=import-error
from pbraiders.pages import sign_in  # pylint: disable=import-error

scenario = partial(scenario, 'contacts/contact_create_failure.feature')


@scenario('Lastname is mandatory')
def test_lastname_is_mandatory() -> None:
    """Lastname is mandatory."""


@scenario('Firstname is mandatory')
def test_firstname_is_mandatory() -> None:
    """Firstname is mandatory."""


@scenario('Phone number is mandatory')
def test_phone_number_is_mandatory() -> None:
    """Phone number is mandatory."""


@given('I am on the new contact page', target_fixture="page_new_contact")
def page_new_contact(the_config, the_browser, the_database) -> ContactNewPage:
    """I am on the new contact page."""
    p_page = ContactNewPage(_driver=the_browser, _config=the_config['urls'])
    if p_page.visit() is False:
        assert sign_in(driver=the_browser, config=the_config, user="simple") is True
        assert p_page.visit() is True
    return p_page


@when('I send the data without the lastname')
def send_data_without_lastname(page_new_contact, the_faker) -> None:
    """I send the data without the lastname."""
    page_new_contact.contact = ContactFakerFactory(_faker=the_faker).initialize(config={})
    p_action = ContactWriteAction(_page=page_new_contact)
    p_action.fill_firstname().fill_phone()
    del p_action
    p_action = ContactCreateAction(_page=page_new_contact)
    p_action.click()


@when('I send the data without the firstname')
def send_data_without_firstname(page_new_contact, the_faker) -> None:
    """I send the data without the firstname."""
    page_new_contact.contact = ContactFakerFactory(_faker=the_faker).initialize(config={})
    p_action = ContactWriteAction(_page=page_new_contact)
    p_action.fill_lastname().fill_phone()
    del p_action
    p_action = ContactCreateAction(_page=page_new_contact)
    p_action.click()


@when('I send the data without the phone number')
def send_data_without_phone_number(page_new_contact, the_faker) -> None:
    """I send the data without the phone number."""
    page_new_contact.contact = ContactFakerFactory(_faker=the_faker).initialize(config={})
    p_action = ContactWriteAction(_page=page_new_contact)
    p_action.fill_lastname().fill_firstname()
    del p_action
    p_action = ContactCreateAction(_page=page_new_contact)
    p_action.click()


@then('I should see the error message')
def error_message(page_new_contact) -> None:
    """I should see the error message."""
    p_action = ContactCreateAction(_page=page_new_contact)
    assert p_action.has_failed() is True
