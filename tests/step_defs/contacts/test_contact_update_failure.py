# coding=utf-8
"""Contact update, failure cases."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.contact import ContactFakerFactory  # pylint: disable=import-error
from pbraiders.pages.contacts.actions import FillContactAction  # pylint: disable=import-error
from pbraiders.pages.contacts.actions import UpdateContactAction  # pylint: disable=import-error
from pbraiders.pages.contacts import ContactPage  # pylint: disable=import-error
from pbraiders.pages import new_contact  # pylint: disable=import-error
from pbraiders.pages import sign_in  # pylint: disable=import-error

scenario = partial(scenario, 'contacts/contact_update_failure.feature')


@scenario('Lastname is mandatory')
def test_lastname_is_mandatory() -> None:
    """Lastname is mandatory."""


@scenario('Firstname is mandatory')
def test_firstname_is_mandatory() -> None:
    """Firstname is mandatory."""


@scenario('Phone number is mandatory')
def test_phone_number_is_mandatory() -> None:
    """Phone number is mandatory."""


@given('I am on the contact page', target_fixture="page_contact")
def page_contact(the_config, the_browser, the_faker, the_database) -> ContactPage:
    """I am on the contact page."""

    # Create new contact
    p_contact = ContactFakerFactory(_faker=the_faker).initialize(config={})
    assert sign_in(driver=the_browser, config=the_config, user="simple") is True
    assert new_contact(driver=the_browser, config=the_config['urls'], contact=p_contact) is True

    # Access the contact page
    p_page = ContactPage(_driver=the_browser, _config=the_config['urls'], _contact=p_contact)
    assert p_page.visit() is True
    assert p_page.is_contact_present() is True

    return p_page


@when('I send the data without the lastname')
def send_data_without_lastname(page_contact, the_faker) -> None:
    """I send the data without the lastname."""
    p_contact = ContactFakerFactory(_faker=the_faker).create(config={})
    p_contact.lastname = ''
    page_contact.set_contact(p_contact)

    # Fill the fields
    p_action = FillContactAction(_page=page_contact)
    p_action.fill_lastname() \
        .fill_firstname() \
        .fill_phone()
    del p_action

    # Update
    p_action = UpdateContactAction(_page=page_contact)
    p_action.update()


@when('I send the data without the firstname')
def send_data_without_firstname(page_contact, the_faker) -> None:
    """I send the data without the firstname."""
    p_contact = ContactFakerFactory(_faker=the_faker).create(config={})
    p_contact.firstname = ''
    page_contact.set_contact(p_contact)

    # Fill the fields
    p_action = FillContactAction(_page=page_contact)
    p_action.fill_lastname() \
        .fill_firstname() \
        .fill_phone()
    del p_action

    # Update
    p_action = UpdateContactAction(_page=page_contact)
    p_action.update()


@when('I send the data without the phone number')
def send_data_without_phone_number(page_contact, the_faker) -> None:
    """I send the data without the phone number."""
    p_contact = ContactFakerFactory(_faker=the_faker).create(config={})
    p_contact.tel = ''
    page_contact.set_contact(p_contact)

    # Fill the fields
    p_action = FillContactAction(_page=page_contact)
    p_action.fill_lastname() \
        .fill_firstname() \
        .fill_phone()
    del p_action

    # Update
    p_action = UpdateContactAction(_page=page_contact)
    p_action.update()


@then('I should see the error message')
def error_message(page_contact) -> None:
    """I should see the error message."""
    p_action = UpdateContactAction(_page=page_contact)
    assert p_action.has_failed() is True
