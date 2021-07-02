# coding=utf-8
"""Contact deletion, cancel cases."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.contact import ContactFakerFactory  # pylint: disable=import-error
from pbraiders.pages.contacts import ContactPage  # pylint: disable=import-error
from pbraiders.pages.contacts.actions import ContactDeleteAction  # pylint: disable=import-error
from pbraiders.pages import new_contact  # pylint: disable=import-error
from pbraiders.pages import sign_in  # pylint: disable=import-error

scenario = partial(scenario, 'contacts/contact_delete_cancel.feature')


@scenario('Not deleting a contact')
def test_not_deleting_a_contact() -> None:
    """Not deleting a contact."""


@given('I am on a contact page', target_fixture="page_contact")
def page_contact(the_config, the_browser, the_faker, the_database) -> ContactPage:
    """I am on the contact page."""

    # Create new contact
    p_contact = ContactFakerFactory(_faker=the_faker).initialize(config={})
    assert sign_in(driver=the_browser, config=the_config, user="simple") is True
    assert new_contact(driver=the_browser, config=the_config['urls'], contact=p_contact) is True

    # Access the contact page
    p_page = ContactPage(_driver=the_browser, _config=the_config['urls'], _contact=p_contact)
    assert p_page.visit() is True

    return p_page


@when('I cancel the deletion of the contact')
def cancel_delete_contact(page_contact) -> None:
    """I cancel the deletion of the contact."""
    p_action = ContactDeleteAction(_page=page_contact)
    p_action.delete().cancel()


@then('I should still access into the contact page')
def still_access(page_contact) -> None:
    """I should still access into the contact page."""
    assert page_contact.visit() is True
