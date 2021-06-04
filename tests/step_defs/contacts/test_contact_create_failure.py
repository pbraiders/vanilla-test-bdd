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
from pbraiders.contacts import PageContactNew  # pylint: disable=import-error
from pbraiders.signin import PageSignin  # pylint: disable=import-error
from pbraiders.signin import sign_in  # pylint: disable=import-error
from pbraiders.user import UserSimpleFactory  # pylint: disable=import-error

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


@when('I send the data without the lastname')
def send_data_without_lastname(page_contact_new, the_faker) -> None:
    """I send the data without the lastname."""
    pFactory = ContactFakerFactory(faker=the_faker)
    page_contact_new.set_contact(pFactory.create(config={})).fill_firstname().fill_phone().click()


@when('I send the data without the firstname')
def send_data_without_firstname(page_contact_new, the_faker) -> None:
    """I send the data without the firstname."""
    pFactory = ContactFakerFactory(faker=the_faker)
    page_contact_new.set_contact(pFactory.create(config={})).fill_lastname().fill_phone().click()


@when('I send the data without the phone number')
def send_data_without_phone_number(page_contact_new, the_faker) -> None:
    """I send the data without the phone number."""
    pFactory = ContactFakerFactory(faker=the_faker)
    page_contact_new.set_contact(pFactory.create(config={})).fill_lastname().fill_firstname().click()


@then('I should see the error message')
def error_message(page_contact_new) -> None:
    """I should see the error message."""
    assert page_contact_new.has_failed() is True
