# coding=utf-8
"""Contact creation, success cases."""

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


@when('I create a new contact')
def contact_new(page_contact_new, the_faker) -> None:
    """I create a new contact."""
    pFactory = ContactFakerFactory(faker=the_faker)
    page_contact_new.set_contact(pFactory.create(config={})) \
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
