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
from pbraiders.contacts import ActionContactFill  # pylint: disable=import-error
from pbraiders.contacts import ActionContactUpdate  # pylint: disable=import-error
from pbraiders.contacts import ContactPage  # pylint: disable=import-error
from pbraiders.contacts import new_contact  # pylint: disable=import-error
from pbraiders.user import UserSimpleFactory  # pylint: disable=import-error

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
    p_contact = new_contact(p_driver=the_browser,
                            a_config=the_config,
                            p_contact_factory=ContactFakerFactory(faker=the_faker),
                            p_user_factory=UserSimpleFactory())

    # Access the contact page
    p_page = ContactPage(browser=the_browser, config=the_config['urls'], contact=p_contact)
    assert p_page.visit() is True
    assert p_page.is_contact_present() is True

    return p_page


@when('I send the data without the lastname')
def send_data_without_lastname(page_contact, the_faker) -> None:
    """I send the data without the lastname."""
    p_Contact = ContactFakerFactory(faker=the_faker).create(config={})
    p_Contact.lastname = ''
    page_contact.set_contact(p_Contact)

    # Fill the fields
    p_page = ActionContactFill(parent=page_contact)
    p_page.fill_lastname() \
        .fill_firstname() \
        .fill_phone()
    del p_page

    # Update
    p_page = ActionContactUpdate(parent=page_contact)
    p_page.update()


@when('I send the data without the firstname')
def send_data_without_firstname(page_contact, the_faker) -> None:
    """I send the data without the firstname."""
    p_Contact = ContactFakerFactory(faker=the_faker).create(config={})
    p_Contact.firstname = ''
    page_contact.set_contact(p_Contact)

    # Fill the fields
    p_page = ActionContactFill(parent=page_contact)
    p_page.fill_lastname() \
        .fill_firstname() \
        .fill_phone()
    del p_page

    # Update
    p_page = ActionContactUpdate(parent=page_contact)
    p_page.update()


@when('I send the data without the phone number')
def send_data_without_phone_number(page_contact, the_faker) -> None:
    """I send the data without the phone number."""
    p_Contact = ContactFakerFactory(faker=the_faker).create(config={})
    p_Contact.tel = ''
    page_contact.set_contact(p_Contact)

    # Fill the fields
    p_page = ActionContactFill(parent=page_contact)
    p_page.fill_lastname() \
        .fill_firstname() \
        .fill_phone()
    del p_page

    # Update
    p_page = ActionContactUpdate(parent=page_contact)
    p_page.update()


@then('I should see the error message')
def error_message(page_contact) -> None:
    """I should see the error message."""
    p_page = ActionContactUpdate(parent=page_contact)
    assert p_page.has_failed() is True
